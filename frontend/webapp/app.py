from flask import Flask, render_template, send_from_directory
import datetime

app = Flask(__name__)

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

if __name__ == '__main__':
    app.debug = True
    app.run()
