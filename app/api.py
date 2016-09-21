#!flask/bin/python
from flask import Response
from flask import request

from app import db, app
import json

class Drug(db.Model):
    object_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(120))
    indicated = db.Column(db.String(120))
    contra_indicated = db.Column(db.String(120))

    def __init__(self, objectId, name, description):
        self.name = name
        self.object_id = objectId
        self.description = description

    # def __repr__(self):
    #     return '<Name %r>' % self.name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @property
    def serialize(self):
        return {
            'objectId': self.object_id,
            'name': self.description,
            'description': self.description,
            'indicated': self.indicated,
            'contraIndicated': self.contra_indicated
        }

@app.route('/', methods=['GET'])
def home():
    result = "Drugster"
    return Response(result, status=200, mimetype='application/json')

@app.route('/all', methods=['GET'])
def all():
    result = json.dumps([obj.serialize for obj in Drug.query.all()], ensure_ascii=False).encode('utf8')
    return Response(result, status=200, mimetype='application/json')

@app.route('/add', methods=['POST'])
def add():
    objectId = request.args.get("objectId")
    name = request.args.get("name")
    description = request.args.get("description")
    indicated = request.args.get("indicated")
    contraIndicated = request.args.get("contraIndicated")

    newToner = Drug(objectId, name, description)
    newToner.indicated = indicated
    newToner.contra_indicated = contraIndicated

    db.session.add(newToner)
    db.session.commit()

    return Response('', status=200, mimetype='application/json')

@app.route('/delete', methods=['GET'])
def delete():
    id = request.args.get('objectId')
    drug = Drug.query.filter_by(object_id=id).first()
    db.session.delete(drug)
    db.session.commit()
    return Response('', status=200, mimetype='application/json')
