from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://nzujzrawszyghk:pd4T9GcZCCBR5WEwbBKR0sqWcW@ec2-54-235-120-118.compute-1.amazonaws.com/d9prntppjn9k5p"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

from app import api
