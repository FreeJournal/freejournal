from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

keyword_association = Table('collection_keywords', Base.metadata,
                            Column('keyword_id', Integer, ForeignKey('keyword.id')),
                            Column('collection_merkle', String, ForeignKey('collection.merkle'))
                            )


class Keyword(Base):
    __tablename__ = 'keyword'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Document(Base):
    __tablename__ = 'document'
    collection_merkle = Column(String, ForeignKey('collection.merkle'))
    description = Column(String)
    hash = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    # Caching information
    filename = Column(String)
    accesses = Column(Integer, nullable=False, default=0)


class Collection(Base):
    __tablename__ = 'collection'
    title = Column(Text, nullable=False)
    description = Column(String)
    merkle = Column(String, primary_key=True)  # Merkle hash of included documents
    address = Column(String, nullable=False)  # Bitmessage address
    version = Column(Integer)
    btc = Column(String)
    keywords = relationship(Keyword, secondary=keyword_association)
    documents = relationship(Document, cascade="all, delete-orphan")
    # Caching information
    creation_date = Column(DateTime, nullable=False)
    accesses = Column(Integer, nullable=False, default=0)
    votes = Column(Integer, nullable=False, default=0)


engine = create_engine('postgres://postgres:password@localhost/freejournal')

Base.metadata.create_all(engine)
