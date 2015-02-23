from sqlalchemy import create_engine
from models import DecBase


def connect_db():
    engine = create_engine('postgres://postgres:password@localhost/freejournal')
    return engine


def setup_db(engine):
    """
    Creates necessary database tables
    :param engine: the database engine to use
    :return:
    """
    DecBase.metadata.create_all(engine)
