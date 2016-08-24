#!flask/bin/python
from flask import render_template

from app import db, app


class Pill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(120))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Name %r>' % self.name

@app.route('/', methods=['GET'])
def home():
    return "Drugster by Squad"

@app.route('/all', methods=['GET'])
def all():
    return render_template('index.html')

@app.route('/squad')
def squad():
    return render_template('base.html')
