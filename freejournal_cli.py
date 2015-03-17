#!/usr/bin/python

import sys, datetime

# BitMessage installer imports
import platform
from bitmessage.install import apt_install, windows_install

# FreeNet installer imports
from freenet.install import linux_install

# FreeJournal library imports
import config
try:
    from cache.cache import Cache
    cache = Cache()
except:
    print ("Warning: SQLite is not installed.  No local cache " \
        + "functionality available.")

try:
    from models.collection import Collection
    from models.keyword import Keyword
    from models.document import Document
except:
    print ("Error: could not import models.")

try:
    from bitmessage.bitmessage_listener import get_collections
    from bitmessage.bitmessage import Bitmessage
    from backend.controller import Controller
except:
    print ("Error: could not import BitMessage dependencies.")

# Frontend imports
try:
    from frontend.webapp import app as webapp
except:
    print ("Error: could not import webapp.")

try:
    # Freenet may not be installed
    import freenet
    from freenet.FreenetConnection import FreenetConnection
    freenet_installed = True
except:
    freenet_installed = False

def print_help():
    """ Print usage instructions for the command-line library. """
    print ("Usage: ./freejournal [command]")
    print ("./freejournal_cli help [command name] - display extended command information.\n")
    print ("Available commands:")
    print ("\tgetdocfile [document hash] [document output path/filename]")
    print ("\tputdoc [document input path]")
    print ("\tlistcollections")
    print ("\tlisten")
    print ("\tinstall [freenet|bitmessage|all]")
    print ("\tshowcollection [index bitmessage ID]")
    print ("\tputcollection [address password] [document IDs, comma separated] [title] [description] [keywords] " \
            + "[Bitcoin address (for rating)]")
    print ("\tpublishcollection [address password] [index bitmessage ID]")

def print_command_help(command):
    """ Display extended help information for CLI command
        :param command: FreeJournal command name"""
    COMMANDS = \
        { "getdocfile": \
            "Get a document with given hash from the FreeJournal network storage.", \
          "putdoc": \
            "Add a document to the FreeJournal network storage and create the local" \
            + " corresponding document object, displaying the document ID required " \
            + " to retreive the document with the configured key.  To publish, " \
            + " call pubcollection with the returned document ID.", \
          "listcollections": \
            "List all document indexes currently known to this FreeJournal instance.", \
          "showcollection": \
            "Display all known details of a given collection, including all documents it indexes.", \
          "listen": \
            "Start the long-running FreeJournal listener.", \
          "install": \
            "Perform initial setup, installing FreeJournal dependencies.", \
          "putcollection": \
            "Create a new collection and store it locally.", \
          "publishcollection": \
            "Publish a local collection to the world (other FreeJournal nodes)." \
        }
    if command in COMMANDS:
        print (COMMANDS[command])
    else:
        print ("Unknown command!")
        print_help()

def get_doc_file(document_hash, document_output_filename):
    """ Get a document file from the Freenet network
        :param document_hash: the Freenet URI to retreive
        :param document_output_filename: path/filename to write to
    """
    freeCon = FreenetConnection()
    output=freeCon.get(document_hash)
    open(document_output_filename, 'w').write(output)
    print ("File with URL " + document_hash + " written to " + document_output_filename)

def list_collections():
    """ List all collections in the local cache """
    print ("Available collections, cached locally: ")
    for collection in cache.get_all_collections():
        print ("\tID " + collection.address + "\t " + collection.title + \
            "\tCreation Date " + collection.creation_date.strftime("%A, %d. %B %Y %I:%M%p"))
        print ("\t" +"~~~~~~~~~~~~~~~Document list~~~~~~~~~~~~~~~")
        print ("\t\t" + "URI" + "\t" + "Title" + "\t" + "Description")
        documents = cache.get_documents_from_collection(collection.address)
        for doc in documents:
            print ("\t\t" + doc.hash + "\t" + doc.title +  "\t" + doc.description)

def list_collection_details(collection_address):
    collection = cache.get_collection_with_address(collection_address)
    if collection is not None:
        print (collection.to_json())
    else:
        print ("Collection not found in local cache.")

def install_dependencies(dependency):
    """ Install a prerequisite (dependency) for deploying a FreeJournal
        node.  Rerun with each FreeJournal upgrade.
        :param dependency: Software to install, freenet/bitmessage/all
    """
    dependency = dependency.lower()
    if dependency == 'freenet' or dependency == 'all':
        os = sys.platform
        if 'linux' not in os:
            raise Exception("Invalid Operating System. See README.")
        else:
            linux_install()
    if dependency == 'bitmessage' or dependency == 'all':
        os_version = platform.dist()[0]
        if 'windows' in os_version:
            windows_install()
        else:
            apt_install()
            print ('Installation Completed')

def put_document(file_path, collection_address, title, description):
    """ Insert a document into the local cache with associated information
        and upload the document to the freenet network.
        :param file_path: the path of the file to upload
        :param collection_address: the collection address associated with the document
        :param title: the title of the document being uploaded
        :param description: the description of the document being uploaded
    """
    file_name = file_path.rsplit('/',1)[0]
    contents = open(file_path).read()
    freeCon = FreenetConnection()
    uri = freeCon.put(contents)
    document = Document(
        collection_address = collection_address,
        description = description,
        hash = uri,
        title = title,
        filename = file_name,
        accesses = 0
    )
    cache.insert_new_document(document)
    print ("Inserted " + file_path + " successfully with URI " + uri)
    print ("Allow up to 10 minutes for file to propogate on the freenet network")

def put_collection(address_password, document_ids, title, description, keywords, btc):
    """ Create a collection in local cache
        :param address_password: The password with which to protect the collection.
        Should be at least 20 characters for optimal security and unique.  Generates 
        the unique collection ID deterministically
        :param document_ids: A list of document object IDs to include in the collection
        :param title: The title of the created collection
        :param description: The description of the created collection
        :param keywords: Comma-separated keywords for the resulting collection
        :param BTC: the Bitcoin address of the resulting collection
    """
    bitmessage_connection = Bitmessage()
    address = bitmessage_connection.create_address(address_password)
    keywords = [Keyword(name=x) for x in keywords.split(",")]
    collection = Collection(
        title=title,
        description=description,
        merkle='I am a merkle',
        address=address,
        version=3,
        btc=btc,
        keywords=keywords,
        documents=[Document(collection_address=address, description="test", hash="asdfasdasdf345fasdaf",
                            title="docTitle", filename="file name", accesses=23)],
        creation_date=datetime.datetime.now(),
        oldest_date=datetime.datetime.now()
    )
    cache.insert_new_collection(collection)
    print ("Collection inserted with address/ID " + address)


def show_collection(collection_address):
    '''
    Displays information about a specific collection, including a document list
    :param collection_address: Collection address
    '''
    collection = cache.get_collection_with_address(collection_address)
    print ("\tID " + collection.address + "\t " + collection.title + \
            "\tCreation Date " + collection.creation_date.strftime("%A, %d. %B %Y %I:%M%p"))
    print ("\t" +"~~~~~~~~~~~~~~~"+ "Document list"+"~~~~~~~~~~~~~~~")
    print ("\t\t" + "URI" + "\t" + "Title" + "\t" + "Description")
    documents = cache.get_documents_from_collection(collection_address)
    for doc in documents:
        print ("\t\t" + doc.hash + "\t" + doc.title +  "\t" + doc.description)

def publish_collection(address_password, collection_address):
    bitmessage_connection = Bitmessage()
    address = bitmessage_connection.create_address(address_password)
    collection = cache.get_collection_with_address(collection_address)
    if collection is not None:
        collection_handler = Controller()
        collection_handler.publish_collection(collection, config.MAIN_CHANNEL_ADDRESS, address)
        print ("Collection published successfully!")
    else:
        print ("Collection not found in local cache.")


def process_command(command):
    """ Process a command-line command and execute the 
        resulting FreeJournal action
        :param command: The command to be executed, as a sys arg array
    """
    if len(sys.argv) < 2:
        print_help()
        return
    command = sys.argv[1].lower()
    if command == 'help':
        if (len(sys.argv) == 3):
            print_command_help(sys.argv[2])
        else:
            print_help()
    elif command == 'getdocfile':
        if (len(sys.argv) == 4):
            get_doc_file(sys.argv[2], sys.argv[3])
        else:
            print_help()
    elif command == 'putdoc':
        if (len(sys.argv)== 6):
            put_document(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
        else:
            print_help()
    elif command == 'listcollections':
        list_collections()
    elif command == 'showcollection':
        if (len(sys.argv)==3):
            show_collection(sys.argv[2])
        else:
            print_help()
    elif command == 'listen':
        get_collections()
    elif command == 'install':
        if (len(sys.argv) == 3):
            install_dependencies(sys.argv[2])
        else:
            print_help()
    elif command == 'putcollection':
        if (len(sys.argv) == 8):
            put_collection(sys.argv[2], \
                sys.argv[3], sys.argv[4], \
                sys.argv[5], sys.argv[6], \
                sys.argv[7])
        else:
            print_help()
    elif command == 'publishcollection':
        if (len(sys.argv) == 4):
            publish_collection(sys.argv[2], sys.argv[3])
        else:
            print_help()
    elif command == 'webapp':
        webapp.app.run(debug = config.WEBAPP_DEBUG)
    else:
        print_help()

if __name__ == '__main__':
    process_command(sys.argv)