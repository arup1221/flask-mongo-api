
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash
from bson.objectid import ObjectId
from users.routes import users_blueprint

app = Flask(__name__)

app.secret_key = "secretkey"

# Configure MongoDB URI
app.config['MONGO_URI'] = 'mongodb+srv://arup:arup2345@cluster0.131i8tz.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)

users_blueprint.mongo = mongo
app.register_blueprint(users_blueprint, url_prefix='/code')
mongo.init_app


@app.route('/', methods=['GET'])
def welcome():
    return '<h1>Welcome to the CRUD api With Flask and MongoDB</h1>', 200


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
