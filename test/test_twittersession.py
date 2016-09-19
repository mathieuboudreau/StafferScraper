import warnings
import unittest
from stafferscraper import twittersession
from stafferscraper.config.loadconfig import load_config

def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        warnings.simplefilter("ignore", ResourceWarning)
        test_func(self, *args, **kwargs)
    return do_test

class LoginTwitterTest(unittest.TestCase):
    
    def setUp(self):
        self.twitter = twittersession.TwitterSession()
        self.BAD_KEY    = 'badkey'
        self.BAD_SECRET = 'badsecret'
        self.userID     = 'RosieBarton'
        
        
        self.configFileName = 'config.yml'
        self.config     = load_config(self.configFileName)
        self.API_KEY    = self.config['API_KEY']
        self.API_SECRET = self.config['API_SECRET']
        
    def tearDown(self):
        pass
    
    @ignore_warnings
    def test_to_verify_if_bad_key_credentials_throw_exception(self):
        self.assertRaises(twittersession.LoginAuthError, self.twitter.login, self.BAD_KEY, self.BAD_SECRET)

    @ignore_warnings
    def test_that_session_instance_variable_is_none_after_login_error(self):
        try:
            self.twitter.login(self.BAD_KEY, self.BAD_SECRET)
        except twittersession.LoginAuthError as e:
            self.assertIsNone(self.twitter.getSession())
    
    @ignore_warnings
    def test_to_verify_that_good_key_credentials_dont_throw_exceptions(self):
        self.twitter.login(self.API_KEY, self.API_SECRET)

    def test_getuserid_returns_the_value_that_was_set(self):
        self.twitter.setUserID(self.userID)
        self.assertEqual(self.userID, self.twitter.getUserID())
        self.twitter.setUserID('')
