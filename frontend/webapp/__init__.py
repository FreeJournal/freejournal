from flask import Flask, render_template, send_from_directory
from make_celery import make_celery
from datetime import timedelta
import datetime
import config
from cache.cache import Cache
from models.collection import Collection
from models.keyword import Keyword
from models.document import Document


app = Flask(__name__, static_folder='public')
app.config.update(
    CELERY_BROKER_URL='amqp://',
    CELERY_RESULT_BACKEND='amqp://',
    CELERYBEAT_SCHEDULE={
        'periodic_test': {
            'task': 'periodic_test',
            'schedule': timedelta(seconds=5),
            'args': (16, 16)
        },
    },
    CELERY_TIMEZONE='UTC'
)
celery = make_celery(app)
cache = Cache()

from tasks.add_task import add_together
from tasks.periodic_test import add_test

documents = [
    {
        "name": "Company, Inc. Hiring Practices",
        "type": "PDF",
        "keywords": ["corporate", "hiring", "leak"],
        "score": "1.243",
        "date": datetime.datetime.now(),
        "submitter": "wafflelover42"
    },
    {
        "name": "Company, Inc. Hiring Practices",
        "type": "PDF",
        "keywords": ["corporate", "hiring", "leak"],
        "score": "1.243",
        "date": datetime.datetime.now(),
        "submitter": "wafflelover42"
    },
    {
        "name": "Company, Inc. Hiring Practices",
        "type": "PDF",
        "keywords": ["corporate", "hiring", "leak"],
        "score": "1.243",
        "date": datetime.datetime.now(),
        "submitter": "wafflelover42"
    },
    {
        "name": "Company, Inc. Hiring Practices",
        "type": "PDF",
        "keywords": ["corporate", "hiring", "leak"],
        "score": "1.243",
        "date": datetime.datetime.now(),
        "submitter": "wafflelover42"
    },
]


@app.route('/')
def index():
    # TODO: Use Flask `g` object to store database connection
    return render_template("index.html", collections=cache.get_all_collections())


@app.route('/c/<string:collection>')
def collection_page(collection):
    return render_template("collection.html", collection=cache.get_collection_with_address(collection))


@app.route('/itest')
def index_test():
    c1 = get_test_collection()
    collections = [
        c1,
        c1,
        c1,
        c1
    ]
    return render_template("index.html", collections=collections)

@app.route('/doctest')
def documents_test():
    c1 = get_test_collection()
    return render_template("collection.html", collection=c1)

@app.route('/public/<path:path>')
def send_static(path):
    return send_from_directory('public', path)


@app.route('/celerytest')
def celery_test():
    result = add_together.delay(23, 42)
    return str(result.wait())


def get_test_collection():
    k1 = Keyword()
    k1.name = "abc"

    k2 = Keyword()
    k2.name = "def"

    d1 = Document()
    d1.description = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    """
    d1.accesses = 0
    d1.collection_address = "abc123"
    d1.filename = "/path/to/file"
    d1.hash = "abc123"
    d1.title = "Important document.pdf"

    c1 = Collection()
    c1.accesses = 0
    c1.address = "abc123"
    c1.btc = "abc123"
    c1.creation_date = datetime.datetime.now()
    c1.description = "Some documents"
    c1.documents = [d1, d1, d1]
    c1.keywords = [k1, k2]
    c1.title = "Document Collection"
    return c1
