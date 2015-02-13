import xmlrpclib
import time
import subprocess
import os
import sys
from config.config import *
from bitmessage_file import BitMessageFile
import base64


class Bitmessage():
    def __init__(self):
        self.os = sys.platform
        print 'Starting BitMessage on ' + self.os

        self.__startup()

    def __startup(self):
        #Try connecting via the api first to see if PyBitmessage is already running
        try:
            self._api_connect()
            assert(5 == self.api.add(2, 3))
        except:
            self._launch_bitmessage()
            self._api_connect()

        #Wait for api to connect to the bitmessage client
        connected = False
        while not connected:
            try:
                assert(5 == self.api.add(2, 3))
                connected = True
            except:
                pass

    print 'Connected successfully'

    def _api_connect(self):
        """Connect to the Bitmessage client
        """
        self.api = xmlrpclib.ServerProxy(BITMESSAGE_SERVER)

    def _launch_bitmessage(self):
        """Used to start up the PyBitmessage client so that we can connect to the api
        """
        if 'linux2' in self.os:
            # Used to ignore the ENORMOUS amount of output from PyBitmessage
            devnull = open(os.devnull, 'wb')

            # Start up PyBitmessage
            subprocess.Popen([RUN_PYBITMESSAGE_LINUX], shell=True, stdout=devnull, stderr=devnull)

    def broadcast(self, label, subject, message):
        """Sends a broadcast to subscribers
        :param label: a valid address label for bitmessage
        :param subject: base64 encoded text
        :param message: base64 encoded text
        """
        broadcast_address = self.api.createRandomAddress(label)
        ack_data = self.api.sendBroadcast(broadcast_address, subject, message)

        print 'Sending Broadcast...'

        status = ''
        while 'sent' not in status:
            status = self.api.getStatus(ack_data)
            print status
            time.sleep(5)


if __name__ == '__main__':
    args = sys.argv

    if len(args) != 2:
        print 'Please pass a path to a file'

    bitmessage = Bitmessage()

    # Create a basic file class
    bitmessage_file = BitMessageFile(args[1])

    file_hash = bitmessage_file.get_hash()
    file_name = bitmessage_file.get_file_name()

    # Construct a new address (testing purposes) and broadcast a test message
    address_label = base64.b64encode(file_name)

    broadcast_subject = base64.b64encode("~Test~")
    broadcast_message = base64.b64encode(file_hash)

    bitmessage.broadcast(address_label, broadcast_subject, broadcast_message)
