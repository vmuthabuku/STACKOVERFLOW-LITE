from flask import Blueprint
from flask import Flask
from flask import request, jsonify, abort, make_response, json
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from passlib.handlers.bcrypt import bcrypt
from routes.Model import insert_user, get_user, post_question, get_questions, get_question, edit_question, delete_question
from ap.models import User, Questions, Answer

che = Blueprint("che",__name__)

@che.route('/api/v2/users/questions', methods=['POST'])
@jwt_required
def question():

    email = get_jwt_identity()
    user = get_user(email)
    # post a single question
    question = Questions(
        question = request.json.get("question"),
        user_id = (user["id"]))
    return jsonify({'Questions': question.__dict__}), 201

@che.route('/api/v2/users/questions', methods=['GET'])
@jwt_required
def view_all_questions():
    email = get_jwt_identity()
    user = get_user(email)

    questions = get_questions(user['id'])
    if questions is None:
    # retrieve all questions
        return jsonify({'message': 'No questions'})
    return jsonify({'Questions': questions}), 200

@che.route('/api/v2/users/questions/<int:id>', methods=['GET'])
@jwt_required
def single_question(id):
    email = get_jwt_identity()
    _user = get_user(email)

    # retrive a question by it's ID
    question = get_question(id)
    if question is None:
        return jsonify({'message': 'Question not available'})

    return jsonify({'Questions': question}), 200

@che.route('/api/v2/users/questions/<int:id>', methods=['PUT'])
@jwt_required
def modify_question(id):
    email = get_jwt_identity()
    _user = get_user(email)
    # Edit a specific question 
    edit = get_question(id)

    if edit is None:
        return jsonify({'message': 'Question not available'})

    edit['question'] = request.json.get('question'),

    edit_question(id, edit)

    return jsonify({'Questions': edit}), 200

@che.route('/api/v2/users/questions/<int:id>', methods=['DELETE'])
@jwt_required
def remove_question(id):
    email = get_jwt_identity()
    _user = get_user(email)
    # Delete a specific question 
    question = get_question(id)
    if question is None:
        return jsonify({'message': 'Question not available'})

    delete_question(id)
    return jsonify({'message': 'Question has been deleted!'}), 200

@che.route('/api/v2/users/questions/<int:id>/answers', methods=['POST'])
@jwt_required
def answer_question(id):
    # retrive a question by it's ID
    _email = get_jwt_identity()
    question = get_question(id)
    # Answer a specific question
    answers = Answer(
        answer = request.json.get("answer"),
        question_id = (question ["id"]))
    answers.save()
    return jsonify({'Answers': answers.__dict__}), 201

