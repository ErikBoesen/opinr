from flask import render_template
from app import app
import json


@app.route('/')
def index():
    # It would probably be more professional to serve data from a Mongo database
    # or something like that, but given the scale of this application I think
    # it's okay to just serve from a JSON file.
    with open('app/data/issues.json', 'r') as f:
        issues = json.load(f)
    return render_template('index.html', issues=issues)
