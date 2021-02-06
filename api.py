import json
import flask
from flask import request, jsonify
from flask_mongoengine import MongoEngine

app = flask.Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'ZanebotDB',
    'host': 'mongodb+srv://admin:jackhammer@cluster0.q0a3b.mongodb.net/ZanebotDB?retryWrites=true&w=majority',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class User(db.Document):
    id = db.StringField()
    name = db.StringField()
    def to_json(self):
        return {"id": self.id,
                "name": self.name}

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    user = User.objects(name=name).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    user = User(name=record['name'],
                id=record['id'])
    user.save()
    return jsonify(user.to_json())

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    user = User.objects(id=record['id']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.update(name=record['name'])
    return jsonify(user.to_json())

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    user = User.objects(id=record['id']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
    return jsonify(user.to_json())

if __name__ == "__main__":
    app.run(debug=True)