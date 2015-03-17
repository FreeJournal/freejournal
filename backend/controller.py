from models.keyword import Keyword
from models.document import Document
from models.collection import Collection
from bitmessage.bitmessage import Bitmessage
from datastructures.fj_message import FJMessage
from cache.cache import Cache
from config import MAIN_CHANNEL_ADDRESS
from jsonschema import *
from models.json_schemas import *
from sqlalchemy.exc import IntegrityError
import json
import time
import base64
import datetime
import hashlib


class Controller:

    def __init__(self):
        self.connection = Bitmessage()
        self.cache = Cache()

    def _check_signature(self, fj_message):
        """
        Checks that the signature is the correct sha256 hash of the address's public keys and payload
        :param fj_message: the message containing the collection and signature
        :return: True if the signatures match, False otherwise
        """



        h = hashlib.sha256(fj_message["pubkey"] + fj_message['payload']).hexdigest()

        if h == fj_message["signature"]:
            print "Signature Verified"
            return True
        else:
            print "Signature Not Verified"
            return False

    def _cache_collection(self, message, payload):
        """
        Checks to see if this collection is already in the cache. If it is we update the collection with the new data.
        Otherwise a new collection is made and cached.
        :param message: the Bitmessage message containing an FJ_message
        :param payload: the contents of the FJ_message
        """
        # Grabbing the text representations of the documents and keywords and rebuilding them
        keywords = []
        docs = []
        for key in payload["keywords"]:
            keywords.append(Keyword(name=key["name"], id=key["id"]))
        for doc in payload["documents"]:
            docs.append(Document(collection_address=doc["address"], description=doc["description"], hash=doc["hash"],
                                 title=doc["title"]))
        cached_collection = self.cache.get_collection_with_address(payload["address"])

        if cached_collection is None:
            collection_model = Collection(
                title=payload["title"],
                description=payload["description"],
                merkle=payload["merkle"],
                address=payload["address"],
                version=payload["version"],
                btc=payload["btc"],
                keywords=keywords, #@todo add keyword support
                documents=docs,
                creation_date=datetime.datetime.strptime(payload["creation_date"], "%A, %d. %B %Y %I:%M%p"),
                oldest_date=datetime.datetime.strptime(payload["oldest_date"], "%A, %d. %B %Y %I:%M%p"),
                latest_broadcast_date=datetime.datetime.strptime(payload["latest_broadcast_date"], "%A, %d. %B %Y %I:%M%p"),
                votes=payload['votes'],
                votes_last_checked=datetime.datetime.strptime(payload["votes_last_checked"], "%A, %d. %B %Y %I:%M%p"),
            )
            try:
                self.cache.insert_new_collection(collection_model)
                print "Cached New Collection"
            except IntegrityError as m:
                #print m.message
                return False
        else:
            cached_collection.update_keywords(keywords)
            cached_collection.title = payload["title"]
            cached_collection.description = payload["description"]
            cached_collection.merkle = payload['merkle']
            cached_collection.address = payload["address"]
            cached_collection.version = payload["version"]
            cached_collection.btc = payload["btc"]
            cached_collection.documents = docs
            cached_collection.creation_date = datetime.datetime.strptime(payload["creation_date"],
                                                                         "%A, %d. %B %Y %I:%M%p")
            cached_collection.oldest_date = datetime.datetime.strptime(payload["oldest_date"], "%A, %d. %B %Y %I:%M%p")
            cached_collection.latest_broadcast_date = datetime.datetime.strptime(payload["latest_broadcast_date"],
                                                                                 "%A, %d. %B %Y %I:%M%p")
            cached_collection.votes = payload['votes']
            cached_collection.votes_last_checked = datetime.datetime.strptime(payload["votes_last_checked"], "%A, %d. %B %Y %I:%M%p")
            try:
                self.cache.insert_new_collection(cached_collection)
                print "Cached Updated Collection"
            except IntegrityError as m:
                #print m.message
                return False
        self.connection.delete_message(message['msgid'])

    def import_collection(self, address):
        """
        Imports a Collection from the given Bit Message address and checks if its signature is valid.
        If it is valid then it is cached locally.
        :param address: the address to import the collection from
        :return: True if the collection was imported and cached successfully, False otherwise
        """

        # buffer time to make sure to get messages
        time.sleep(10)
        messages = self.connection.check_inbox()
        for message in messages["inboxMessages"]:
            if message["toAddress"] == address:
                # decoded_message is a FJMessage
                base64_decode = base64.b64decode(message["message"])
                try:
                    json_decode = json.loads(base64_decode)
                    validate(json_decode, fj_schema)
                except (ValueError, TypeError, ValidationError) as m:
                    #print m.message
                    print "Not a FJ Message or Invalid FJ Message"
                    continue

                # Trying to filter out non collection messages
                # TODO Change this?
                if "payload" in json_decode:
                    payload = json_decode["payload"]
                    try:
                        payload = json.loads(payload)
                        validate(payload, coll_schema)
                    except (ValueError, TypeError, ValidationError) as m:
                        #print m.message
                        print "Contents of FJ Message invalid or corrupted"
                        continue

                    if self._check_signature(json_decode):
                        self._cache_collection(message, payload)
                        return True

        #print "Could not import collection"
        return False

    def publish_collection(self, collection, to_address, from_address):
        """
        Publishes the given to collection to the bitmessage network
        :param collection: the collection to be published
        :param to_address: the address to send the collection to,  always MAIN_CHANNEL_ADDRESS except in unittests
        :param from_address: the address to send the collection from
        :return: True if the collection is published successfully, False otherwise
        """
        collection_payload = collection.to_json()
        if collection_payload is None:
            return False
        new_fj_message = FJMessage(1, collection.address, collection_payload)
        sendable_fj_message = new_fj_message.to_json()
        if sendable_fj_message is None:
            return False
        self.connection.send_message(to_address, from_address, "subject", sendable_fj_message)
        return True
