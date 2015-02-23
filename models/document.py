from sqlalchemy import Column, ForeignKey, Integer, String
from models import DecBase


class Document(DecBase):
    """ A document represents a single document shared to the network.
        Documents are indexed by tuples contained in their respective collections.
        Documents are stored and retreived from the Freenet network using the hashes
        in the index, and if full caching is enables, are cached on disk according
        to their age and the number of accesses tracked on this node.
    """
    # Required for relationships
    __tablename__ = 'document'
    collection_address = Column(String, ForeignKey('collection.address'))
    """The address of the Collection the document is contained in. @todo investigate multiple collections"""
    description = Column(String)
    """The description of the document as stored in the latest known DocIndex"""
    hash = Column(String, primary_key=True)
    """The SHA-256 hash of this document"""
    title = Column(String, nullable=False)
    """The title of the document as stored in the latest known DocIndex"""

    # Caching information (for pruning)
    filename = Column(String)
    """The document filename on disk, or None if not stored"""
    accesses = Column(Integer, nullable=False, default=0)
    """The number of accesses the document has received on the FreeJournal network"""
