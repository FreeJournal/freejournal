import sys
from bitmessage.bitmessage import Bitmessage
from backend.controller import Controller
from models.keyword import Keyword
from models.document import Document
from models.collection import Collection
import datetime

if __name__ == '__main__':
    args = sys.argv

    #Create a bitmessage connection
    bitmessage_connection = Bitmessage()
    collection_handler = Controller()

    address_label = "Test Collection"
    address = bitmessage_connection.create_address(address_label)

    collection_test = Collection(
        title="Title Test",
        description="Description Test",
        merkle='I am a merkle',
        address=address,
        version=3,
        btc="btc-123abcasdfasd",
        keywords=[Keyword(name="First"), Keyword(name="Second")],
        documents=[Document(collection_address=address, description="test", hash="asdfasdasdf345fasdaf",
                            title="docTitle", filename="file name", accesses=23)],
        creation_date=datetime.datetime.now(),
        oldest_date=datetime.datetime.now()
    )

    collection_handler.publish_collection(collection_test, address)
