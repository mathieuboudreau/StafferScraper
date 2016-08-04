import unittest
from stafferscraper import twittersession

class LoginTwitterTest(unittest.TestCase):
    
    def setUp(self):
        self.twitter = twittersession.TwitterSession()
        self.BAD_KEY    = 'badkey'
        self.BAD_SECRET = 'badsecret'
        
    def tearDown(self):
        pass
    
    def test_to_verify_if_bad_key_credentials_throw_exception(self):
        
        self.assertRaises(twittersession.LoginAuthError, self.twitter.login, self.BAD_KEY, self.BAD_SECRET)
