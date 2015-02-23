from sqlalchemy.orm import sessionmaker
from db import setup_db, connect_db
from models.collection import Collection
from models.document import Document
from models.keyword import Keyword

engine = connect_db()
setup_db(engine)
DBSession = sessionmaker(bind=engine)


def create_session():
    return DBSession()


def get_all_collections():
    session = create_session()
    return session.query(Collection).order_by(Collection.creation_date.desc())


def get_collection_with_address(address):
    session = create_session()
    return session.query(Collection).filter(Collection.address == address).one()


def insert_new_collection(collection):
    session = create_session()
    session.add(collection)
    session.commit()
