from collection import *
from FJMessage.fj_message import *

import json
from bitmessage.bitmessage import *
from bitmessage.config.config import *
import hashlib
import base64


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
        h = hashlib.sha256(fj_message["payload"] + address).hexdigest()
        if h == fj_message["signature"]:
            print "Signature Verified"
            return True
        else:
            print "Signature Not Verified"
            return False

    def import_collection(self, address):
        """
        Imports a Collection from the given Bit Message address and checks if its signature is valid
        :param address: the address to import the collection from
        :return: A Collection object gathered from the Bit Message payload if successful,
        an error message otherwise
        """
        self.connection.subscribe(address)
        messages = self.connection.check_inbox()

        for message in messages:
            #decoded_message is a FJMessage
            decoded_message = base64.b64decode(message["message"])
            #Trying to filter out spam and non collection messages
            # TODO Change this filtering technique?
            if "type_id" in decoded_message["payload"] and decoded_message["payload"]["type_id"] == 1:
                if self._check_signature(decoded_message, address):
                    payload = decoded_message["payload"]
                    return Collection(payload["type_id"], payload["title"], payload["description"],
                                      payload["keywords"],payload["collection_address"],
                                      payload["documents"], payload["merkle"], payload["btc"], payload["version"])
        print "Could Not Import Collection"

    def create_collection(self, title, description, keywords, documents, address_label):
        """
        Creates a new,empty collection and sends its Bit Message address to the main channel
        :param title: the title of the collection
        :param description: the description of the collection
        :param keywords: the keywords that apply to this collection
        :param documents: the FreeNet document addresses
        :param address_label: the label for the new Bit Message address
        :return: a new Collection object
        """
        new_address = self.connection.create_address(address_label)
        new_collection = Collection(1, title, description, keywords, new_address, 1)
        collection_payload = new_collection.to_json()
        new_fj_message = FJMessage(1, new_address, collection_payload )
        self.connection.send_message(MAIN_CHANNEL_ADDRESS, new_address, "New Collection - " + title, new_fj_message)
        self.connection.send_broadcast(new_address, "New Collection - " + title, new_fj_message)
        return new_collection


