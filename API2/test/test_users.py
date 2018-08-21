import unittest
import os
import json

class StackOverflow_lite_Users(unittest.TestCase):
    """This class represent Users."""
    def setUp(self):
        """Define test variables and initialize."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.users = {'name': 'vincent', 'email': 'vm@email.com', 'password': 'let me pass'}
    def test_signup_users(self):
        response =  self.client.post(
            '/api/v2/auth/signup',data = json.dumps(self.users), content_type = 'application/json')
        self.assertEqual(response.status_code,200)        )
    
    def test_signin_user(self):
        """Test to login a registered user."""
        response = self.client.post(
            '/api/v2/auth/signin', data=json.dumps(self.users), content_type='application/json')
        self.assertEqual(response.status_code, 200)
if __name__ == "__main__":
    unittest.main() 
