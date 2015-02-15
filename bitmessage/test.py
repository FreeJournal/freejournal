import sys
from bitmessage import Bitmessage

if __name__ == '__main__':
    args = sys.argv

    #Create a bitmessage connection
    bitmessage_connection = Bitmessage()

    # Construct a new address (testing purposes)
    address_label = "Test Label"
    address = bitmessage_connection.create_address(address_label)

    # Construct a message to send
    subject = "~Test~"
    message = "Test Message"

    #Send a test broadcast
    bitmessage_connection.send_broadcast(address, subject, message)

    #Send a test message
    bitmessage_connection.send_message(address, address, subject, message)