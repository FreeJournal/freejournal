''' URL to use for the SQLAlchemy engine.
    By default, the Postgres database is used and required.
    Feel free to change this to any of the commented, alternate
    URL's to change database management systems.
''' 
# DB_URL = 'postgres://postgres:password@localhost/freejournal'
# DB_URL = 'mysql://scott:tiger@localhost/foo'
DB_URL = 'sqlite:///fj.db'

''' Caching strategy.
    'all': attempt to mirror all documents within diskspace constraints
    ('blacklist', [address array]): don't mirror collections on blacklist array
    ('whitelist', [address array]): don't mirror collections on blacklist array'''
MIRROR_STRATEGY = 'all'
# MIRROR_STRATEGY = ('blacklist', ['BM-1EXAMPLE'])

''' Max disk space to use.  Allowable units are G and M.'''
MAX_DISKSPACE = '5G'
