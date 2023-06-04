import os
import unittest
from unittest.mock import patch

from your_app import app  # replace 'your_app' with the name of your app script file

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.patcher1 = patch('stripe.OAuth.authorize_url')
        self.patcher2 = patch('stripe.OAuth.token')
        self.patcher3 = patch('stripe.OAuth.deauthorize')
        self.MockAuthorize = self.patcher1.start()
        self.MockToken = self.patcher2.start()
        self.MockDeauthorize = self.patcher3.start()

    def tearDown(self):
        self.patcher1.stop()
        self.patcher2.stop()
        self.patcher3.stop()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Connect with Stripe', response.data)

    def test_authorize(self):
        self.MockAuthorize.return_value = 'http://example.com'
        response = self.app.get('/authorize')
        self.assertEqual(response.status_code, 302)
        self.assertIn('http://example.com', response.location)

    def test_callback_success(self):
        self.MockToken.return_value = {'stripe_user_id': 'test_stripe_user_id'}
        response = self.app.get('/oauth/callback?code=test_code')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Success! Account', response.data)

    def test_callback_failure(self):
        self.MockToken.side_effect = stripe.oauth_error.OAuthError
        response = self.app.get('/oauth/callback?code=test_code')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error:', response.data)

    def test_deauthorize_success(self):
        self.MockDeauthorize.return_value = None
        response = self.app.get('/deauthorize?stripe_user_id=test_stripe_user_id')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Success! Account', response.data)

    def test_deauthorize_failure(self):
        self.MockDeauthorize.side_effect = stripe.oauth_error.OAuthError
        response = self.app.get('/deauthorize?stripe_user_id=test_stripe_user_id')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error:', response.data)


if __name__ == '__main__':
    unittest.main()
