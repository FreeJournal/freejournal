#!/usr/bin/python

import sys, datetime, uuid, argparse, platform, types

from helpers import get_doc_file, put_document, list_collections, list_collection_version, list_collection_details, show_collection, install_dependencies, put_collection, publish_collection
import config


class HelpfulParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        exit(2)

# Base parser
parser = HelpfulParser(description="FreeJournal Client")
subparsers = parser.add_subparsers(help="FreeJournal client command", dest="command", metavar="<command>")

# Subcommand parsers
# getdoc
parser_getdoc = subparsers.add_parser("getdoc",
                                      help="get a document with given hash\n \n from the FreeJournal\n network storage")
parser_getdoc.add_argument("hash", type=str, help="hash of the document to get")
parser_getdoc.add_argument("output_path", type=str, help="path to save the document to")
parser_getdoc.parents = [parser_getdoc]
subparsers._choices_actions[0].metavar = "getdoc [-h] hash output_path"

# putdoc
parser_putdoc = subparsers.add_parser("putdoc",
                                      help="add a document to the FreeJournal network storage and create the local"
                                           + " corresponding document object, displaying the document ID required "
                                           + " to retrieve the document with the configured key.  To publish, "
                                           + " use the `pubcollection` command with the returned document ID.")
parser_putdoc.add_argument("path", type=str, help="path of the document to upload")
parser_putdoc.add_argument("address", type=str, help="BitMessage address of the collection to add this document to")
parser_putdoc.add_argument("title", type=str, help="title of the document")
parser_putdoc.add_argument("description", type=str, help="description of the document")
subparsers._choices_actions[1].metavar = "putdoc [-h] path address title description"

# listcollections
parser_listcollections = subparsers.add_parser("listcollections",
                                               help="list all document indexes currently known to this FreeJournal"
                                                    + " instance")

# listversions
parser_listversions = subparsers.add_parser("listversions", help="list all the versions of a particular collection")
parser_listversions.add_argument("address", help="BitMessage address of the collection")
parser_listversions.add_argument("-d", "--documents", action="store_true", dest="show_documents",
                                 help="print document_ids")
subparsers._choices_actions[3].metavar = "listversions [-h] [-d] address"

# listen
parser_listen = subparsers.add_parser("listen", help="start the long-running FreeJournal listener")

# install
parser_install = subparsers.add_parser("install", help="install FreeJournal dependencies")
parser_install.add_argument("deps", choices=["freenet", "bitmessage", "all"], help="dependencies to install")
subparsers._choices_actions[5].metavar = "install [-h] deps"

# showcollection
parser_showcollection = subparsers.add_parser("showcollection", help="display all known details of a given collection,"
                                                                     + " including all documents it indexes")
parser_showcollection.add_argument("address", help="BitMessage address of the collection")
subparsers._choices_actions[6].metavar = "showcollection [-h] address"

# putcollection
parser_putcollection = subparsers.add_parser("putcollection", help="create a new collection and store it locally")
parser_putcollection.add_argument("address_password", help="the password with which to protect the collection")
parser_putcollection.add_argument("title", help="title for the new collection")
parser_putcollection.add_argument("description", help="description for the new collection")
parser_putcollection.add_argument("keywords", help="comma-separated keywords")
parser_putcollection.add_argument("btc_address", help="Bitcoin address for donations")
subparsers._choices_actions[7].metavar = "putcollection [-h] address_password title description keywords btc_address"

# publishcollection
parser_publishcollection = subparsers.add_parser("publishcollection", help="publish a local collection to the world"
                                                                           + "(other FreeJournal nodes)")
parser_publishcollection.add_argument("address_password", help="the password for this collection")
parser_publishcollection.add_argument("id", help="the BitMessage ID for this collection")
subparsers._choices_actions[8].metavar = "publishcollection [-h] address_password id"

# webapp
parser_webapp = subparsers.add_parser("webapp", help="run the HTTP server front end")

# uploader
parser_uploader = subparsers.add_parser("uploader", help="run the uploader GUI application")

# keepalive
parser_keepalive = subparsers.add_parser("keepalive", help="run the keep-alive function to help sustain the FreeJournal"
                                                           + " network")


def process_command():
    """ Process a commafrend-line command and execute the
        resulting FreeJournal action
        :param command: The command to be executed, as a sys arg array
    """
    args = parser.parse_args()
    command = args.command
    if command == 'getdoc':
        get_doc_file(args.hash, args.output_path)
    elif command == 'putdoc':
        put_document(args.path, args.address, args.title, args.description)
    elif command == 'listcollections':
        list_collections()
    elif command == 'listversions':
        list_collection_version(args.address, args.show_documents)
    elif command == 'showcollection':
        show_collection(args.address)
    elif command == 'listen':
        from bitmessage.bitmessage_listener import get_collections
        get_collections()
    elif command == 'install':
        install_dependencies(args.deps)
    elif command == 'putcollection':
        put_collection(args.address_password, args.title, args.description, args.keywords, args.btc_address)
    elif command == 'publishcollection':
        publish_collection(args.address_password, args.id)
    elif command == 'webapp':
        import frontend.webapp.app as webapp
        webapp.run(debug=config.WEBAPP_DEBUG, port=config.WEBAPP_PORT)
    elif command == 'uploader':
        from frontend.uploader import fjUploaderGUI
        fjUploaderGUI.run()
    elif command == 'keepalive':
        from bitmessage.bitmessage_keepalive import find_old_collections
        find_old_collections(3)
