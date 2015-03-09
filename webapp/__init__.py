from flask import Flask, render_template, send_from_directory
from make_celery import make_celery
from datetime import timedelta
import datetime

app = Flask(__name__)
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
    return render_template("index.html", documents=documents)


@app.route('/public/<path:path>')
def send_static(path):
    return send_from_directory('public', path)


@app.route('/celerytest')
def celery_test():
    result = add_together.delay(23, 42)
    return str(result.wait())
