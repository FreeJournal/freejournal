from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Table
from sqlalchemy.orm import relationship
from models import DecBase
from models.document import Document
from models.keyword import Keyword

keyword_association = Table('collection_keywords', DecBase.metadata,
                            Column('keyword_id', Integer, ForeignKey('keyword.id')),
                            Column('collection_address', String, ForeignKey('collection.address'))
                            )


class Collection(DecBase):
    __tablename__ = 'collection'
    title = Column(Text, nullable=False)
    description = Column(String)
    merkle = Column(String, nullable=False)  # Merkle hash of included documents
    address = Column(String, primary_key=True)  # Bitmessage address
    version = Column(Integer)
    btc = Column(String)
    keywords = relationship(Keyword, secondary=keyword_association)
    documents = relationship(Document, cascade="all, delete-orphan")
    # Caching information
    creation_date = Column(DateTime, nullable=False)
    accesses = Column(Integer, nullable=False, default=0)
    votes = Column(Integer, nullable=False, default=0)
