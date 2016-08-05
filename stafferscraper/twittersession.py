import twython
from twython import Twython

class TwitterSession:
    def __init__(self):
        self._session = None

    def login(self, APP_KEY, APP_SECRET):
        '''Login to Twitter API
        Uses OAuth2 authentication
        '''
        
        try:
            self._session = Twython(APP_KEY, APP_SECRET, oauth_version=2)
            self._session.verify_credentials() # Should throw exception for bad keys
            
        except twython.exceptions.TwythonAuthError:
            self._session = None
            raise LoginAuthError("Bad Twitter API login credentials")
     
    def getSession(self):
        return self._session
            
class LoginAuthError(twython.exceptions.TwythonAuthError):
    '''Throw exception for bad authentication
    Wrapper class for Twython's authentication error
    '''
    def __init__(self,*args,**kwargs):
        twython.exceptions.TwythonAuthError.__init__(self,*args,**kwargs)