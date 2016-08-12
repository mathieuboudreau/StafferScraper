import os
import sqlite3

class TweetDB:
    '''Tweet Database Class
    To handle pushing/fetching tweet data to a local database using sqlite3
    
    -args-
        twitterHandle: string, twitter handle of the user-of-interest for this db
    '''
    
    dbFolder = 'databases/' # Default class folder to store databases. 
                            # If you want a different folder, ensure you
                            # set the class variable after you import it.
                            #
                            # e.g. from tweetdb import TweetDB
                            #      TweetDB.dbFolder = 'newfolder/'

    dbFileExtension = '.db'     # See previous comment for similar handling

    def __init__(self,twitterHandle):
        self._dbConnection = None
        self._dbCursor = None
        
        if not os.path.exists(TweetDB.dbFolder):
            os.makedirs(TweetDB.dbFolder)
            
        self._dbConnection = sqlite3.connect(TweetDB.dbFolder + twitterHandle + TweetDB.dbFileExtension)
        self._dbCursor = self._dbConnection.cursor()
        
    def __del__(self):
        self._dbConnection.close()   
