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

@bPrint.route('/api/v2/users/questions', methods=['POST'])
@jwt_required
def question():

    email = get_jwt_identity()
    user = get_user(email)
    # post a single question
    question = Questions(
        question = request.json.get("question"),
        user_id = (user["id"]))
    question.save()
    return jsonify({'Questions': question.__dict__}), 201

@bPrint.route('/api/v2/users/questions', methods=['GET'])
@jwt_required
def view_all_questions():
    email = get_jwt_identity()
    user = get_user(email)

    questions = get_questions(user['id'])
    if questions is None:
    # retrieve all questions
        return jsonify({'message': 'No questions found'})
    return jsonify({'Questions': questions}), 200

@bPrint.route('/api/v2/users/questions/<int:id>', methods=['GET'])
@jwt_required
def single_question(id):
    email = get_jwt_identity()
    user = get_user(email)

    # retrive a question by it's ID
    question = get_question(id)
    if question is None:
        return jsonify({'message': 'Question not available'})

    return jsonify({'Questions': question}), 200

