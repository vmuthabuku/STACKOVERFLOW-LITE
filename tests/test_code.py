import unittest
import os
import json

from app.code import create_app
from app.models import Question, Answer

class StackOverflow_lite(unittest.TestCase):
    """This class represents Questions and Answers posted."""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.questions = {'Question': 'What is a flask restful api'}
        self.answers = {'Answer': 'flask restful is a python framework?'}
        
    def test_post_question(self):
        """Testing posting a question."""
        response = self.client.post(
            '/api/v1/questions', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_view_all_questions(self):
        """Test to view all questions."""
        response = self.client.get(
            '/api/v1/questions', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_view_single_question(self):
        """Test view a single question."""
        response = self.client.get(
            '/api/v1/questions/1', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_edit_question(self):
        """Test can edit a question."""
        self.client.post(
            '/api/v1/questions', data=json.dumps(self.questions), content_type='application/json')
        response = self.client.put(
            '/api/v1/questions/1', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_delete_question(self):
        """Test delete a question."""
        response = self.client.get(
            '/api/v1/questions/1', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/v1/questions/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_answer_question(self):
        """Test answer a question."""
        response = self.client.post(
            '/api/v1/questions/1/answers', data=json.dumps(self.answers), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_question_does_not_exist(self):
        """Test question does not exist."""
        response = self.client.get(
            '/api/v1/questions/12121', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code,200)
        data = json.loads(response.data.decode('UTF-8'))
        self.assertEqual(data['Message'], "No question found")
        
if __name__ == "__main__":
    unittest.main()