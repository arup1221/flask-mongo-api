from flask import Blueprint, jsonify, request
# from . import mongo
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash
from bson.objectid import ObjectId



users_blueprint = Blueprint('users', __name__)

mongo = PyMongo()


@users_blueprint.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']

    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)

        user = {
            'name': _name,
            'email': _email,
            'pwd': _hashed_password
        }

        # Insert the user into the MongoDB collection
        id = mongo.db.users.insert_one(user).inserted_id

        resp = jsonify(
            {"message": "User added successfully", "id": str(id)})
        resp.status_code = 200
        return resp
    else:
        return not_found(404)


@users_blueprint.route('/users', methods=['GET'])
def get_all_users():
    users = mongo.db.users.find()
    user_list = []
    for user in users:
        user['_id'] = str(user['_id'])
        user_list.append(user)
    return jsonify(users=user_list)


@users_blueprint.route('/users/<id>', methods=['GET'])
def get_user_by_id(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)
    else:
        return not_found(404)


@users_blueprint.route('/users/<id>', methods=['PUT'])
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


@users_blueprint.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = mongo.db.users.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
        resp = jsonify(message="User deleted successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found(404)


def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url
    }

    resp = jsonify(message)
    resp.status_code = 404

    return resp
