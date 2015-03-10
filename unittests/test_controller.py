import unittest
from backend.controller import Controller
from models.collection import Collection
from models.keyword import Keyword
from models.document import Document
import uuid
import datetime
import time



class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()
        self.address = self.controller.connection.create_address('Controller Test address')
        coll_address = str(uuid.uuid1())
        doc_hash_1 = str(uuid.uuid1())
        doc_hash_2 = str(uuid.uuid1())
        doc_hash_3 = str(uuid.uuid1())
        self.test_collection = Collection(
            title="Test",
            description="This is a collection!",
            merkle="123456789",
            address=self.address,
            version=1,
            btc="123456789",
            keywords=[
                Keyword(name="Keyword A", id=109),
                Keyword(name="Keyword B", id=110),
            ],
            documents=[
                Document(
                    description="Test document A",
                    hash=doc_hash_1,
                    title="Test A",
                    ),
                Document(
                    description="Test document B",
                    hash=doc_hash_2,
                    title="Test B",
                    ),
            ],
            creation_date=datetime.datetime.now(),
            oldest_date=datetime.datetime.now()
        )

        self.test_collection_updated = Collection(
            title="Test",
            description="This is a collection! and its updated",
            merkle="123456789",
            address=self.address,
            version=1,
            btc="123456789",
            keywords=[
                Keyword(name="Keyword A", id=109),
                Keyword(name="Keyword B", id=110),
                Keyword(name="Keyword C", id=111)
            ],
            documents=[
                Document(
                    description="Test document A",
                    hash=doc_hash_1,
                    title="Test A",
                    ),
                Document(
                    description="Test document B",
                    hash=doc_hash_2,
                    title="Test B",
                    ),
                Document(
                    description="Test document C",
                    hash=doc_hash_3,
                    title="Test B",
                    )
            ],
            creation_date=datetime.datetime.now(),
            oldest_date=datetime.datetime.now()
        )

    def tearDown(self):
        self.controller = None

    def test_publish_and_import_collection(self):
        self.controller.publish_collection(self.test_collection, self.address, self.address)
        timeout = 600  # 10 minutes
        start_time = time.time()
        curr_time = time.time()

        sent = False
        while curr_time - start_time < timeout:
            sent = self.controller.import_collection(self.address)
            if sent:
                break
            curr_time = time.time()
            time.sleep(1)
        coll = self.controller.cache.get_collection_with_address(self.address)
        self.assertEqual(coll.title, 'Test')
        self.assertEqual(coll.btc, '123456789')
        self.assertEqual(coll.description, 'This is a collection!')
        self.assertEqual(coll.address, self.address)
        self.controller.publish_collection(self.test_collection_updated, self.address, self.address)

        timeout = 600  # 10 minutes
        start_time = time.time()
        curr_time = time.time()

        sent = False
        while curr_time - start_time < timeout:
            sent = self.controller.import_collection(self.address)
            if sent:
                break
            curr_time = time.time()
            time.sleep(1)
        coll = self.controller.cache.get_collection_with_address(self.address)
        self.assertEqual(coll.title, 'Test')
        self.assertEqual(coll.btc, '123456789')
        self.assertEqual(coll.description, 'This is a collection! and its updated')
        self.assertEqual(coll.address, self.address)
        self.assertEqual(3, len(coll.documents))
        self.assertEqual(3, len(coll.keywords))