from flask import Blueprint
from flask import Flask
from flask import request, jsonify, abort, make_response, json
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from passlib.handlers.bcrypt import bcrypt
from Models.Model import insert_user, get_user, post_question, get_questions, get_question, edit_question, delete_question
from models import User, Questions, Answer

bPrint = Blueprint("bPrint",__name__)

@bPrint.route('/api/v2/auth/signup', methods=['POST'])
def signup_user():
    user = get_user(request.json.get('email'))
    if user is not None:
        return jsonify({'message': "Email already exists."})

    user = User(name = request.json.get("name"),
                email = request.json.get("email"),
                password = bcrypt.encrypt(request.json.get("password")))
    user.save()

    return jsonify({'message': 'New user registered!', 'User': user.__dict__})

@bPrint.route('/api/v2/auth/signin', methods=['POST'])
def signin():
    email = request.json.get("email")
    password = request.json.get("password")

    user = get_user(email)
    if user is None:
        return jsonify({"message": "Email not found"}), 404
    elif not bcrypt.verify(password, user['password']):
        return jsonify({'message': "Incorrect password"}), 400
    else:
        token = create_access_token(identity=request.json.get('email'))
        return jsonify({'message': 'Logged in successfully!', 'token': token})
    return make_response('Your account does not exist!, Please Register!'), 401


