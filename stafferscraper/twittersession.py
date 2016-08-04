import twython
from twython import Twython

class TwitterSession:
    def __init__(self):
        self.session = None

    def login(self, APP_KEY, APP_SECRET):
        '''Login to Twitter API
        Uses OAuth2 authentication
        '''
        
        try:
            self.session = Twython(APP_KEY, APP_SECRET, oauth_version=2)
            self.session.verify_credentials() # Should throw exception for bad keys
            
        except twython.exceptions.TwythonAuthError:
            raise LoginAuthError("Bad Twitter API login credentials")
        
class LoginAuthError(twython.exceptions.TwythonAuthError):
    '''Throw exception for bad authentication
    Wrapper class for Twython's authentication error
    '''
    def __init__(self,*args,**kwargs):
        twython.exceptions.TwythonAuthError.__init__(self,*args,**kwargs)