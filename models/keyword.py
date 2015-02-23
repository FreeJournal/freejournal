from sqlalchemy import Column, Integer, String
from models import DecBase


class Keyword(DecBase):
    __tablename__ = 'keyword'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
