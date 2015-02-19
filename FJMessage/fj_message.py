import datetime
import hashlib


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
        self.time_created = datetime.datetime.now.time()
        self.payload = payload

    def generate_signature(self):
        """
        Generates a sha256 signature of the address sending the message
        and the payload of the message
        """
        self.signature = hashlib.sha256(self.original_sender + self.payload).hexdigest()