import json


class Collection():

    def __init__(self, type_id, title, description, keywords, collection_address, version, btc=None, documents=[],
                 merkle=None):
        """
        Constructor for a Collection object
        :param type_id: 1, denotes this is a collection
        :param title: the title of the collection
        :param description: the description of the collection
        :param keywords: the keywords that apply to this collection
        :param collection_address: the Bit Message address for this collection
        :param version: the version number of this collection
        :param btc: the bitcoin address for this collection
        :param documents: the FreeNet document addresses
        :param merkle: the merkle root of the document hashes of this collection
        """
        self.type_id = 1
        self.title = title
        self.description = description
        self.keywords = keywords
        self.collection_address = collection_address
        self.version = version
        self.btc = btc
        self.documents = documents
        self.merkle = merkle

    def add_document(self, document):
        """
        Adds a FreeNet document address to this collection and updates the merkle tree
        :param document: the address to be added
        """
        self.documents.append(document)
        self.update_merkle()

    def to_json(self):
        """
        Creates a json encoding to be hashed, used by signature generation
        :return: the json encoding of the collection
        """
        return json.dumps({"type_id": self.type_id, "title": self.title, "description": self.description,
                           "keywords": self.keywords, "address": self.collection_address, "documents":
                            self.documents, "merkle": self.merkle, "btc": self.btc, "version": self.version},
                          sort_keys=True)

    def update_merkle(self):
        """
        Updates the collection's merkle tree
        """
        # TODO implement merkle trees and this function
        return False