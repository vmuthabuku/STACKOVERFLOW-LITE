"""This is a python flask app to check for endpoints"""

from flask import request, jsonify, abort, Flask

# local import
from instance.config import app_config

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    
    questions = []
    answers = []

    @app.route('/api/v1/questions', methods=['POST'])
    def question():
        #pylint: disable=unused-variable
        """Returns a created question"""
        question = {'id': len(questions)+1,
            'Questions': request.json.get('Question'),
        }
        questions.append(question)
        return jsonify({'Message': "Question successfully created"} ,{'Questions': questions}), 201

    @app.route('/api/v1/questions', methods=['GET'])
    def view_all_questions():
        #pylint: disable=unused-variable
        """Returns all questions asked by the user"""
        return jsonify({'Questions': questions}), 200

    @app.route('/api/v1/questions/<int:id>', methods=['GET'])
    def single_question(id):
        #pylint: disable=unused-variable
        """Returns specific and single question by its id"""
        single_question = [question for question in questions if question['id'] == id]
        if len(single_question) == 0:
            return jsonify({'Message': "No question found"})

        return jsonify({'Questions': single_question}), 200

    @app.route('/api/v1/questions/<int:id>', methods=['PUT'])
    def edit_question(id):
        #pylint: disable=unused-variable
        """Returns the edited question"""
        edit_question = [question for question in questions if question['id'] == id]
        if len(edit_question) == 0:
            return jsonify({'Message': "No question found"})
        edit_question = {
            'Question': request.json.get('Question'),
        }
        return jsonify({'Questions': edit_question}), 200

    @app.route('/api/v1/questions/<int:id>', methods=['DELETE'])
    def delete_question(id):
        #pylint: disable=unused-variable
        """Returns the deleted question """
        delete_question = [question for question in questions if question['id'] == id]
        if len(delete_question) == 0:
            return jsonify({'Message':"No question found"})

        questions.remove(delete_question[0])

        return jsonify({'Questions': questions}), 200

    @app.route('/api/v1/questions/<int:id>/answers', methods=['POST'])
    def answer_question(id):
        #pylint: disable=unused-variable
        """Checks for a question by its Id"""
        question = [question for question in questions if question['id'] == id]
        if len(question) == 0:
            return jsonify({'Message': "No question found"})
        """Returns the answer to the specific question"""
        answer_question = {'id': len(answers)+1,
            'Answer': request.json.get('Answer')
        }
        answers.append(answer_question)
        return jsonify({'Question': question}, {'Answers': answer_question}), 201


    return app