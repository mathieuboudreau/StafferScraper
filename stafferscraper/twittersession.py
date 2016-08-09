import twython
from twython import Twython

class TwitterSession:
    def __init__(self):
        self._session = None
        self._userID = ''
        
    def login(self, API_KEY, API_SECRET):
        '''Login to Twitter API
        Uses OAuth2 authentication
        '''
        
        try:
            self._session = Twython(API_KEY, API_SECRET, oauth_version=2)
            self._ACCESS_TOKEN = self._session.obtain_access_token() # Should throw exception for bad keys
            self._session = Twython(API_KEY, access_token = self._ACCESS_TOKEN) 
            self._session.show_user(screen_name = 'twitter') # Fetch Twitter's user profile to ensure access token is valid

        except twython.exceptions.TwythonAuthError:
            self._session = None
            raise LoginAuthError("Bad Twitter API login credentials")
    
    # Get/Set methods 
    def getSession(self):
        return self._session
    
    def setUserID(self, userID):
        self._userID = userID
        
    def getUserID(self):
        return self._userID

class LoginAuthError(twython.exceptions.TwythonAuthError):
    '''Throw exception for bad authentication
    Wrapper class for Twython's authentication error
    '''
    def __init__(self,*args,**kwargs):
        twython.exceptions.TwythonAuthError.__init__(self,*args,**kwargs)