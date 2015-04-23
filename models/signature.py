from sqlalchemy import Column, ForeignKey, Integer, String
from models import DecBase


class Signature(DecBase):
    """ A signature validates the contents of a collection.

        Attributes:

    """
    __tablename__ = 'signature'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pubkey = Column(String)
    signature = Column(String)
    address = Column(String, ForeignKey('collection.address'))