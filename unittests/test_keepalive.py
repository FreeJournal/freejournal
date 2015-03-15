from cache.cache import Cache
from models.collection import Collection
from bitmessage.bitmessage_keepalive import find_old_collections
import datetime
import unittest


class TestKeepalive(unittest.TestCase):
    def setup(self):
        cache = Cache()


        collection1 = Collection(
            title="First Collection",
            merkle="Test",
            address="bm-first",
            keywords=[],
            documents=[],
            latest_broadcast_date=datetime.datetime.today(),
            creation_date=datetime.datetime.today(),
            oldest_date=datetime.datetime.today(),
            accesses=0,
            votes=0
        )

        cache.insert_new_collection(collection1)

        collection2 = Collection(
            title="Second Collection",
            merkle="Test",
            address="bm-second",
            keywords=[],
            documents=[],
            latest_broadcast_date=datetime.datetime.today() - datetime.timedelta(days=2),
            creation_date=datetime.datetime.today(),
            oldest_date=datetime.datetime.today(),
            accesses=0,
            votes=0
        )

        cache.insert_new_collection(collection2)

        collection3 = Collection(
            title="Third Collection",
            merkle="Test",
            address="bm-third",
            keywords=[],
            documents=[],
            latest_broadcast_date=datetime.datetime.today() - datetime.timedelta(days=1),
            creation_date=datetime.datetime.today(),
            oldest_date=datetime.datetime.today(),
            accesses=0,
            votes=0
        )

        cache.insert_new_collection(collection3)

        collection4 = Collection(
            title="Fourth Collection",
            merkle="Test",
            address="bm-fourth",
            keywords=[],
            documents=[],
            latest_broadcast_date=datetime.datetime.today() - datetime.timedelta(days=6),
            creation_date=datetime.datetime.today(),
            oldest_date=datetime.datetime.today(),
            accesses=0,
            votes=0
        )

        cache.insert_new_collection(collection4)

    def test_bitmessage_keepalive(self):
        num_collections = find_old_collections(3)
        self.assertTrue(num_collections == 2)

suite = unittest.TestLoader().loadTestsFromTestCase(TestKeepalive)
unittest.TextTestRunner(verbosity=2).run(suite)