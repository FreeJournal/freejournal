from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from db import setup_db, connect_db
from models.collection import Collection

engine = connect_db()
setup_db(engine)
DBSession = sessionmaker(bind=engine)


class Cache():
    """
    A Cache is an object used to communicate with the sqlalchemy database.

    Attributes:
        session: the sqlalchemy session for this Cache
    """
    def __init__(self):
        """
        Create a new database session to support
        insertion or removal of local data.
        """
        self.session = DBSession()

    def get_all_collections(self):
        """
        Get all collections currently stored locally
        :return: list of collections, ordered by date added
        """
        return self.session.query(Collection).order_by(Collection.creation_date.desc())

    def get_collection_with_address(self, address):
        """
        Retreive a specific collection as it's stored locally
        :param address: the collection BitMessage address to retreive
        :return: Collection object with desired ID in latest local state, or None if no Collection found
        """
        row = None
        try:
            row = self.session.query(Collection).filter(Collection.address == address).one()
        except NoResultFound:
            pass
        return row

    def insert_new_collection(self,collection):
        """
        Insert a new collection into local storage
        :param collection: Collection object to insert into local storage
        """
        self.session.add(collection)
        self.session.commit()
