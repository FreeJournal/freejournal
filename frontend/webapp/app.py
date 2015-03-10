from flask import Flask, render_template, send_from_directory
import datetime
import config

# FreeJournal imports
from cache.cache import Cache

app = Flask(__name__, static_folder = 'public')
cache = Cache()

@app.route('/')
def index():
    return render_template("index.html", collections=cache.get_all_collections())

@app.route('/public/<path:path>')
def send_static(path):
    return send_from_directory('public', path)
