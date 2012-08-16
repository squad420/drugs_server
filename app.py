import os

from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class Pill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(120))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route('/', methods=['GET', 'POST'])
@app.route('/drugs', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/squad')
def squad():
    return render_template('base.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5036))
    app.run(host='127.0.0.1', port=port, debug=True)
