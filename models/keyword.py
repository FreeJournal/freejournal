from sqlalchemy import Column, Integer, String
from models import DecBase


class Keyword(DecBase):
    """ A keyword, used for search (one class per unique keyword)

        Attributes:
            id: The identifier for this keyword
            name: The keyword itself, as a string of max-length 50
    """
    __tablename__ = 'keyword'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
