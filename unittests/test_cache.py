import unittest
import datetime

from cache.models import Document, Collection, Keyword
from cache.cache import insert_new_collection, DBSession


class TestCache(unittest.TestCase):
    def setUp(self):
        session = DBSession()
        c = session.query(Collection).all()
        k = session.query(Keyword).all()
        d = session.query(Document).all()
        for coll in c:
            session.delete(coll)
        for key in k:
            session.delete(key)
        for doc in d:
            session.delete(doc)
        session.commit()

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
        session = DBSession()
        coll = session.query(Collection).filter(Collection.merkle == "123456789").one()
        self.assertEquals(coll.title, "Test")
        doc = session.query(Document).filter(Document.hash == "321454213").one()
        self.assertEquals(doc.title, "Test B")
