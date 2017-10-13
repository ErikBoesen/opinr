from flask import render_template
from app import app

@app.route('/')
def index():
	issues = ['Marijuana Legalization', 'Prison Reform']
	return render_template('index.html')

@app.route('/view/<id>/')
def view(id):
	return render_template('view.html')
