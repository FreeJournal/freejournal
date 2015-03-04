from global_imports import *
import json
import hashlib
import time
import base64
import datetime


class CollectionHandler:

    def __init__(self):
        self.connection = Bitmessage()

    def _check_signature(self, fj_message, address):
        """
        Checks that the signature is the correct sha256 hash of the address and payload
        :param fj_message: the message containing the collection and signature
        :param address:  the address this collection came from
        :return: True if the signatures match, False otherwise
        """

        h = hashlib.sha256(fj_message["original_sender"] + fj_message['payload']).hexdigest()
        if h == fj_message["signature"]:
            print "Signature Verified"
            return True
        else:
            print "Signature Not Verified"
            return False

    def _collection_tojson(self, collection):
        """
        Encodes a Collection as a json representation so it can be sent through the bitmessage network

        :param collection: The Collection to be encoded
        :return: the json representation of the given Collection
        """
        docs = collection.documents
        json_docs = []
        for doc in docs:
            json_docs.append((doc.collection_address, doc.description, doc.hash, doc.title))
        keywords = collection.keywords
        json_keywords = []
        for key in keywords:
            json_keywords.append((key.id, key.name))
        return json.dumps({"type_id": 1, "title": collection.title, "description": collection.description,
                           "keywords": json_keywords, "address": collection.address, "documents": json_docs,
                           "merkle": collection.merkle, "btc": collection.btc, "version": collection.version,
                           "creation_date": collection.creation_date.strftime("%A, %d. %B %Y %I:%M%p"),
                           "oldest_date": collection.oldest_date.strftime("%A, %d. %B %Y %I:%M%p")},
                          sort_keys=True)

    def import_collection(self, address):
        """
        Imports a Collection from the given Bit Message address and checks if its signature is valid.
        If it is valid then it is cached locally.
        :param address: the address to import the collection from
        :return: True if the collection was imported and cached successfully, False otherwise
        """
        self.connection.subscribe(address)
        # buffer time to make sure to get messages
        time.sleep(10)
        messages = self.connection.check_inbox()

        for message in messages["inboxMessages"]:

            if message["toAddress"] == address:

                # decoded_message is a FJMessage
                base64_decode = base64.b64decode(message["message"])
                try:
                    json_decode = json.loads(base64_decode)
                except (ValueError, TypeError):
                    print "Not a FJ Message or Invalid FJ Message"
                    continue

                # Trying to filter out non collection messages
                # TODO Change this filtering technique?
                if "payload" in json_decode and self._check_signature(json_decode, address):

                    payload = json_decode["payload"]
                    try:
                        payload = json.loads(payload)
                    except (ValueError, TypeError):
                        print "Contents of FJ Message invalid or corrupted"
                        continue

                    # Grabbing the text representations of the documents and keywords and rebuilding them
                    keywords = []
                    docs = []
                    for key in payload["keywords"]:
                        keywords.append(Keyword(name=key[1], id=key[0]))
                    for doc in payload["documents"]:
                        docs.append(Document(collection_address=doc[0], description=doc[1], hash=doc[2], title=doc[3]))

                    collection_model = Collection(
                        title=payload["title"],
                        description=payload["description"],
                        merkle='test',
                        address=payload["address"],
                        version=payload["version"],
                        btc=payload["btc"],
                        keywords=keywords,
                        documents=docs,
                        creation_date=datetime.datetime.strptime(payload["creation_date"], "%A, %d. %B %Y %I:%M%p"),
                        oldest_date=datetime.datetime.strptime(payload["oldest_date"], "%A, %d. %B %Y %I:%M%p")
                    )

                    insert_new_collection(collection_model)
                    self.connection.delete_message(message['msgid'])
                    print "Collection cached"
                    return True

        print "Could not import collection"

    def publish_collection(self, collection, address=''):
        """
        Publishes the given to collection to the bitmessage network
        :param title: the title of the collection
        :param description: the description of the collection
        :param keywords: the keywords that apply to this collection
        :param documents: the FreeNet document addresses
        :param address_label: the label for the new Bit Message address
        """

        collection_payload = self._collection_tojson(collection)
        new_fj_message = FJMessage(1, collection.address, collection_payload)
        new_fj_message.generate_signature()
        sendable_fj_message = new_fj_message.to_json()

        self.connection.send_message(MAIN_CHANNEL_ADDRESS, address, "subject", sendable_fj_message)
