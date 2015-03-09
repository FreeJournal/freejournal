from global_imports import *
import json
import hashlib
import time
import base64
import datetime
from backend.bmaddresses import *


class Controller:

    def __init__(self):
        self.connection = Bitmessage()

    def _check_signature(self, fj_message):
        """
        Checks that the signature is the correct sha256 hash of the address's public keys and payload
        :param fj_message: the message containing the collection and signature
        :param address:  the address this collection came from
        :return: True if the signatures match, False otherwise
        """

        h = hashlib.sha256(fj_message["pubkey"] + fj_message['payload']).hexdigest()

        if h == fj_message["signature"]:
            print "Signature Verified"
            return True
        else:
            print "Signature Not Verified"
            return False

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
                # TODO Change this?
                if "payload" in json_decode:

                    payload = json_decode["payload"]
                    try:
                        payload = json.loads(payload)
                    except (ValueError, TypeError):
                        print "Contents of FJ Message invalid or corrupted"
                        continue

                    if self._check_signature(json_decode):
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
                        cached_collection = get_collection_with_address(payload["address"])
                        insert_new_collection(collection_model)
                        self.connection.delete_message(message['msgid'])
                        print "Collection cached"
                        return True

        print "Could not import collection"
        return False

    def publish_collection(self, collection, address=''):
        """
        Publishes the given to collection to the bitmessage network
        :param collection: the collection to be published
        :param address: the address to send the collection to
        """

        collection_payload = collection.to_json()
        new_fj_message = FJMessage(1, collection.address, collection_payload)

        sendable_fj_message = new_fj_message.to_json()

        self.connection.send_message(MAIN_CHANNEL_ADDRESS, address, "subject", sendable_fj_message)
