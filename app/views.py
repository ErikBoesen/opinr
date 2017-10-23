from flask import render_template
from app import app
import json


@app.route('/')
def index():
    with open('app/data/issues.json', 'r') as f:
        issues = json.load(f)
    return render_template('index.html', issues=issues)
