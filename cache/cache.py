from sqlalchemy.orm import sessionmaker
from db import setup_db, connect_db
from models.collection import Collection
from models.document import Document
from models.keyword import Keyword

engine = connect_db()
setup_db(engine)
DBSession = sessionmaker(bind=engine)

def create_session():
    """
    Create a new database session to support
    insertion or removal of local data.
    :return: new database session created
    """
    return DBSession()


def get_all_collections():
    """
    Get all collections currently stored locally
    :return: list of collections, ordered by date added
    """
    session = create_session()
    return session.query(Collection).order_by(Collection.creation_date.desc())

def get_collection_with_address(address):
    """
    Retreive a specific collection as it's stored locally
    :param address: the collection BitMessage address to retreive
    :return: Collection object with desired ID in latest local state
    """
    session = create_session()
    return session.query(Collection).filter(Collection.address == address).one()


def insert_new_collection(collection):
    """
    Insert a new collection into local storage
    :param collection: Collection object to insert into local storage
    """
    session = create_session()
    session.add(collection)
    session.commit()
