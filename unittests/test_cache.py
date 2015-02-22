import unittest
import datetime

from cache.models import Document, Collection, Keyword
from cache.cache import insert_new_collection


class TestCache(unittest.TestCase):
    def test_create_collection(self):
        coll = Collection(
            title="Test",
            description="This is a collection!",
            merkle="123456789",
            address="123456789",
            version=1,
            btc="123456789",
            keywords=[
                Keyword(name="Keyword A"),
                Keyword(name="Keyword B"),
            ],
            documents=[
                Document(
                    description="Test document A",
                    hash="123456789",
                    title="Test A",
                    ),
                Document(
                    description="Test document B",
                    hash="321454213",
                    title="Test B",
                    ),
            ],
            creation_date=datetime.datetime.now()
        )
        insert_new_collection(coll)
