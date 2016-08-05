import unittest
from stafferscraper import twittersession

class LoginTwitterTest(unittest.TestCase):
    
    def setUp(self):
        self.twitter = twittersession.TwitterSession()
        self.BAD_KEY    = 'badkey'
        self.BAD_SECRET = 'badsecret'
        self.userID     = 'RosieBarton'
        
    def tearDown(self):
        pass
    
    def test_to_verify_if_bad_key_credentials_throw_exception(self):
        self.assertRaises(twittersession.LoginAuthError, self.twitter.login, self.BAD_KEY, self.BAD_SECRET)

    def test_that_session_instance_variable_is_none_after_login_error(self):
        try:
            self.twitter.login(self.BAD_KEY, self.BAD_SECRET)
        except twittersession.LoginAuthError as e:
            self.assertIsNone(self.twitter.getSession())
    
    def test_getuserid_returns_the_value_that_was_set(self):
        self.twitter.setUserID(self.userID)
        self.assertEqual(self.userID, self.twitter.getUserID())
        self.twitter.setUserID('')
