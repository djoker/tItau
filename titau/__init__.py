__version__ = '0.1.0'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tItau.db'
db = SQLAlchemy(app)

