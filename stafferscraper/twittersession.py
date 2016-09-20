import twython
from twython import Twython

class TwitterSession:
    def __init__(self):
        self.__session = None
        self.__userID = ''
        
    def login(self, API_KEY, API_SECRET):
        '''Login to Twitter API
        Uses OAuth2 authentication
        '''
        
        try:
            self.__session = Twython(API_KEY, API_SECRET, oauth_version=2)
            self.__ACCESS_TOKEN = self.__session.obtain_access_token() # Should throw exception for bad keys
            self.__session = Twython(API_KEY, access_token = self.__ACCESS_TOKEN)
            self.__session.show_user(screen_name = 'twitter') # Fetch Twitter's user profile to ensure access token is valid

        except twython.exceptions.TwythonAuthError:
            self.__session = None
            raise LoginAuthError("Bad Twitter API login credentials")
    
    # Get/Set methods 
    def getLatestTweet(self):
        tweet = self.__session.get_user_timeline(screen_name = self.__userID, count=1)
        return tweet[0]

    def getTweetBatch(self, maxID):
        return self.__session.get_user_timeline(screen_name = self.__userID, count=200, max_id=maxID)

    def getSession(self):
        return self.__session
    
    def setUserID(self, userID):
        self.__userID = userID
        
    def getUserID(self):
        return self.__userID

class LoginAuthError(twython.exceptions.TwythonAuthError):
    '''Throw exception for bad authentication
    Wrapper class for Twython's authentication error
    '''
    def __init__(self,*args,**kwargs):
        twython.exceptions.TwythonAuthError.__init__(self,*args,**kwargs)