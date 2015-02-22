from models import Document, Collection, engine
from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker(bind=engine)


def get_all_collections():
    session = DBSession()
    return session.query(Collection).order_by(Collection.creation_date.desc())


def get_collection_with_merkle(merkle):
    session = DBSession()
    return session.query(Collection).filter(Collection.merkle == merkle).one()


def insert_new_collection(collection):
    session = DBSession()
    session.add(collection)
    session.commit()
