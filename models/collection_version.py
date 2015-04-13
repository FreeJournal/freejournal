from sqlalchemy import Column, Integer, String
from models import DecBase


class CollectionVersion(DecBase):
	'''
	As new collections get added to the Freejournal network, the old collections are
	stored in the cache. When a collection is updated, or modified, a new master hash
	is generated to identify the collection. When this happens, a CollectionVersion
	object is made to store the state of the old collection
	'''
	__tablename__ = 'collectionversion'
	rootHash = Column(String, primary_key=True)
	documentString = Column(String, nullable = False)
	CollectionVersion = Column(Integer, nullable =False)