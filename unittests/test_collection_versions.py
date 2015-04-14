from cache.cache import Cache
from models.collection import Collection
from controllers import collections
import unittest
import datetime

class TestCollectionHistory(unittest.TestCase):
    def setUp(self):
    	cache = Cache()
    	cache.reset_database()
        self.collection1 = Collection(
            title="First Cdollection",
            btc="btc",
            address="bm-first",
            description="description",
            keywords=[],
            documents=[],
            latest_broadcast_date=datetime.datetime.today(),
            creation_date=datetime.datetime.today(),
            oldest_date=datetime.datetime.today(),
            latest_btc_tx="",
            oldest_btc_tx="",
            accesses=0,
            votes=0,
            votes_last_checked=datetime.datetime.today()
        )

        cache.insert_new_collection(self.collection1)

        self.collection2 = Collection(
            title="Secondd Collection",
            btc="btc",
            address="bm-second",
            description="description",
            keywords=[],
            documents=[],
            latest_broadcast_date=datetime.datetime.today() - datetime.timedelta(days=3),
            creation_date=datetime.datetime.today(),
            oldest_date=datetime.datetime.today(),
            latest_btc_tx="",
            oldest_btc_tx="",
            accesses=0,
            votes=0,
            votes_last_checked=datetime.datetime.today()
        )

        cache.insert_new_collection(self.collection2)

    def test_empty_version(self):
    	cache = Cache()
    	versions = cache.get_versions_for_collection(self.collection1.address)
    	if(len(versions)!=0):
    		self.fail("Version should be empty to start")

 	def test_incrementing(self):
   		cache = Cache()
   		cache.reset_database()
   		versions = cache.get_versions_for_collection(self.collection1.address)
   		if(len(versions)!=0):
   			self.fail("Version should be nonzero")
   		collections.update_hash(self.collection1)
   		versions = cache.get_versions_for_collection(self.collection1.address)
   		if(versions[0].collection_version!=1):
   			self.fail("Incorrect collection version")

    def test_version_update(self):
    	cache = Cache()
    	collections.update_hash(self.collection1)
    	versions = cache.get_versions_for_collection(self.collection1.address)
    	if(len(versions)!=1):
    		self.fail("Version should be updated")
    	if(versions[0].collection_address!=self.collection1.address):
    		print(versions[0].collection_address)
    		print(self.collection1.address)
    		self.fail("Wrong collection address")

if __name__ == '__main__':
    unittest.main()