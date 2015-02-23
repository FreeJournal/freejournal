from sqlalchemy import Column, ForeignKey, Integer, String
from models import DecBase


class Document(DecBase):
    __tablename__ = 'document'
    collection_address = Column(String, ForeignKey('collection.address'))
    description = Column(String)
    hash = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    # Caching information
    filename = Column(String)
    accesses = Column(Integer, nullable=False, default=0)
