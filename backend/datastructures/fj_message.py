import datetime
import hashlib
import json
import os
from backend.bmaddresses import *


class FJMessage():

    def __init__(self, type_id, original_sender, payload):
        """
        FJMessage constructor. Signature is empty at first and a call to generate signature required
        before the message is sent on the Bit Message network, Change this?
        :param type_id: type of message being sent, 1=Collection, 2=Document, 3=Rebroadcast Request
        :param original_sender: the Bit Message address of the user sending this message
        :param payload: the content of this message
        """
        # TODO change signature generation?
        self.protocol = "FJ1.0"
        self.type_id = type_id
        self.original_sender = original_sender
        self.signature = ''
        self.time_created = datetime.datetime.now()
        self.payload = payload

    def generate_signature(self):
        """
        Generates a sha256 signature of the public keys
        and the payload of the message
        """
        to_status, to_address_version_number, to_stream_number, to_ripe = decodeAddress(self.original_sender)
        self.signature = hashlib.sha256(to_ripe.encode('hex') + self.payload).hexdigest()

    def to_json(self):
        """
        Creates a json encoding to be sendable in a Bit Message,
        :return: the json encoding of the message
        """
        return json.dumps({"protocol": self.protocol, "type_id": self.type_id, "original_sender": self.original_sender,
                           "signature": self.signature, "time_created": self.time_created.strftime("%A, %d. %B %Y %I:%M%p"),
                           "payload": self.payload}, sort_keys=True)