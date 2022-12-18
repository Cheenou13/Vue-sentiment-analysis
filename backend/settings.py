
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

import nltk

# nltk.download()
# simple representation fo backend (no data base created)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:'cheenou13'@localhost/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

