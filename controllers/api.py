
import datetime


class Resource(object):
    signature = None
    timeCreated = None
    description = ""

    def __init__(self, signature, description):
            self.originalSender = originalSender
            self.signature = signature
            self.timeCreated = datetime.datetime.now.time()
            self.description = description


class Document(Resource):
    title = ""
    description = ""
    timestamp = None
    payload = None
    documentHash = None
    freeNetAddress = None
    collectionAddress = None

    def __init__(
        self,
        signature,
        description,
        payload,
        title,
        timestamp,
            collectionAddress):
        Resource.__init__(self, signature, timeCreated, description)
        self.title = title
        self.timestamp = timestamp
        self.payload = payload
        self.documentHash = hash(payload)
        self.collectionAddress = collectionAddress


class Collection(Resource):
    title = ""
    keywords = []
    merkleHash = None
    documents = []
    btcID = None
    collectionAddress

    def __init__(
        self,
        signature,
        description,
        btcID,
        keywords,
            collectionAddress):
        Resource.__init__(self, signature, description)
        self.btcID = btcID
        self.keywords = keywords
        self.collectionAddress = collectionAddress

    def addDocument(document):
        documents.add(document)


def getDocument(hash):
    """Inward Facing
       This function retrives the document associated with the supplied SHA256 hash.
       Every document has a unique documentHash that can be used to uniquely identify
       and retrieve the indexing information (and subsequently) the document from
       other nodes on the BitMessage Network.
       To find the document assuming the information is not indexed locally, the
       calling node will have to query (over bitmessage) the other nodes for its
       existence. If one of the nodes has recieved the information in the past
       TTL (usually 2 days), the node will broadcast the indexing information for the
       document, allowing the request for indexing info to be completed.
       Once the original node has the indexing information (the path to the data itself),
       the node will connect to freenode and use the supplied index to retrieve the payload.
       :param hash: documentHash
       :return: None"""
    return None


def createDocument(
    signature,
    description,
    payload,
    title,
    timestamp,
        collectionAddress):
     """Outward Facing
        Add a document to the FreeJournal Network
        To do this controllers, the document is first uploaded to FreeNet. Once there, the file
        is associated with a freeNetAddress (like a URL) which is stored with the additional indexing
        information and is distrubted (via a broadcast on Bitmessage) to the FreeJournal network.
        :param signature: The private-key signed hash of the document, proving its authenticity. If
                          the decrypted(with the collections public key) data is equal to the hash of
                          the payload, we know the data is assured authenticity
        :param description: a description of the contents of the document being uploaded
        :param payload: The binary/text data that is to be uploaded\
        :param title: The title of the document
        :param timestamp: The Bitcoin signed time stamp, assuring the document's timeliness/existence
        :param collectionAddress: The address of the collection the document is being published to.
                                  This address is the BitMessage broadcast address for the collection
        :return: new Document"""
    return Document(signature, description, payload, title, timestamp, collectionAddress)

def createCollection(
    signature,
    description,
    btcID,
    keywords,
        collectionAddress):
     """Outward Facing
        A function nodes use to create new collections to publish documents to.
        To do this a Bitmessage broadcast address is supplied, as well as a signature to identify the
        users that have the right to write to the collection.

        :param signature: The private-key signed hash of the collectionAddress, proving its authenticity.
                          Note, since there is no payload for the initial createCollection, a signed hash
                          of the collectionAddress will act as the initial signature. The signature will
                          have to be verified immediately upon creation
        :param description: description of the collection that is being createDocument
        :param btcID: bitcoin transaction ID used to verify the collection
        :param keywords: a String-list of keywords associated with the collectoin used for internal indexing
        :param collectionAddress: The  address of the collection. The address is the public broadcast address
                                  or the BitMessage protocol.
        :return: new collection"""
    return COllection(signature, description, btcID, keywords, collectionAddress)


def importCollection(randomNonce, password):
    """Inward Facing
       Let FreeJournal nodes to retrieve an entire collection that is not on their local machine. 
       To do this the randomNone and password are combined in order to regenerate a Public/Private 
       key pair. This keypair is associated with the collection and
       the other nodes can be queried accordingly."""
