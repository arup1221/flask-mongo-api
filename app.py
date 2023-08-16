
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash
from bson.objectid import ObjectId

app = Flask(__name__)

app.secret_key = "secretkey"

# Configure MongoDB URI
app.config['MONGO_URI'] = 'mongodb+srv://arup:arup2345@cluster0.131i8tz.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def welcome():
    return '<h1>Welcome to the CRUD api With Flask and MongoDB</h1>', 200


@app.route('/users', methods=['POST'])  # endpoint /users
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)

        user = {
            'name': _name,
            'email': _email,
            'password': _hashed_password
        }

        id = mongo.db.users.insert_one(user).inserted_id

        resp = jsonify({"message": "User added successfully", "id": str(id)})
        resp.status_code = 200
        return resp
    else:
        return not_found(400)


@app.route('/users', methods=['GET'])  # endpoin /users
def get_all_users():
    users = mongo.db.users.find()
    user_list = []
    for user in users:
        user['_id'] = str(user['_id'])
        user_list.append(user)
    return jsonify(users=user_list)


@app.route('/users/<id>', methods=['GET'])  # endpoint /users/<id>
def get_user_by_id(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)
    else:
        return not_found(404)


@app.route('/users/<id>', methods=['PUT'])  # endpoint /users/<id>
def update_user(id):
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password and request.method == 'PUT':
        _hashed_password = generate_password_hash(_password)

        mongo.db.users.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'name': _name, 'email': _email, 'password': _hashed_password}}
        )

        resp = jsonify(message="User updated successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found(400)


@app.route('/users/<id>', methods=['DELETE'])  # endpoint /users/<id>
def delete_user(id):
    result = mongo.db.users.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
        resp = jsonify(message="User deleted successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found(404)


@app.errorhandler(400)
def bad_request(error=None):
    message = {
        'status': 400,
        'message': 'Bad Request: ' + request.url
    }

    resp = jsonify(message)
    resp.status_code = 400

    return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url
    }

    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
