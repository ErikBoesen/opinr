from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('configuration.ProductionConfig')
app.config.from_object('app.configuration.DevelopmentConfig')
#app.config.from_object('configuration.TestingConfig')
app.config.setdefault('CACHE_TYPE', 'null')

db = SQLAlchemy(app)

from app import views
