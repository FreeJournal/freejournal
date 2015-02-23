from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Table
from sqlalchemy.orm import relationship
from models import DecBase
from models.document import Document
from models.keyword import Keyword

# Define foreign keys required for joining defined tables together
keyword_association = Table('collection_keywords', DecBase.metadata,
                            Column('keyword_id', Integer, ForeignKey('keyword.id')),
                            Column('collection_address', String, ForeignKey('collection.address'))
                            )


class Collection(DecBase):
    """ A Collection is the fundamental unit of organization in the FreeJournal network.
        A Collection is a uniquely identifiable set of documents.  Each collection is associated
        with and signed by a BitMessage broadcast channel address.  Each collection contains
        a list of documents, a Bitcoin address for ranking, and a version.  Messages on the network
        called DocIndex messages share the state of a collection at a given version.

        This class stores the latest version of each collection the FreeJournal node decides to mirror.
        It also stores old timestamps and Merkle trees for bookkeeping purposes (@todo).

        Attributes:
            title: Title of collection (as in message spec)
            description: Collection description (as in message spec)
            merkle: Merkle hash of latest known version (as in message spec)
            address: Bitmessage address uniquely ID'ing collection (as in message spec)
            version: Current collection version (as in message spec)
            btc: Bitcoin address for rating documents (as in message spec)
            keywords: Keywords as list of Keyword class for searching (as in message spec)
            documents: List of document classes included in the collection (as in message spec)
            creation_date: Earliest known timestamp of collection, or if none earliest approximation of creation date of
                current version of collection
            oldest_date: Earliest known timestamp of collection, or if none earliest approximation of creation date of
                any version of collection
            latest_btc_tx: Latest Bitcoin transaction timestamping merkle belonging to this collection
            oldest_btc_tx: Oldest Bitcoin transaction timestamping merkle belonging to this collection
            accesses: Number of times this collection is accessed by a user of this node (for cache pruning)
            votes: Latest vote count from the Bitcoin network, used to rank collection
            votes_last_checked: Latest poll of Bitcoin network for collection votes, to coordinate internal repolling
    """
    __tablename__ = 'collection'
    title = Column(Text, nullable=False)
    description = Column(String)
    merkle = Column(String, nullable=False)
    address = Column(String, primary_key=True)
    version = Column(Integer)
    btc = Column(String)
    keywords = relationship(Keyword, secondary=keyword_association)
    documents = relationship(Document, cascade="all, delete-orphan")
    creation_date = Column(DateTime, nullable=False)
    oldest_date = Column(DateTime, nullable=False)
    latest_btc_tx = Column(String)
    oldest_btc_tx = Column(String)
    accesses = Column(Integer, nullable=False, default=0)
    votes = Column(Integer, nullable=False, default=0)
    votes_last_checked = Column(DateTime)
