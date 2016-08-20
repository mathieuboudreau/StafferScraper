import os
import sqlite3

class TweetDB:
    '''Tweet Database Class
    To handle pushing/fetching tweet data to a local database using sqlite3
    
    -args-
        twitterHandle: string, twitter handle of the user-of-interest for this db
        
    -Table Format-
        (id INTEGER UNIQUE, created_at TIMESTAMP, text VARCHAR(140)
    '''
    
    dbFolder = 'databases/' # Default class folder to store databases. 
                            # If you want a different folder, ensure you
                            # set the class variable after you import it.
                            #
                            # e.g. from tweetdb import TweetDB
                            #      TweetDB.dbFolder = 'newfolder/'

    dbFileExtension = '.db'     # See previous comment for similar handling

    def __init__(self,twitterHandle):
        self.__dbConnection = None
        self.__dbCursor = None
        
        if not os.path.exists(TweetDB.dbFolder):
            os.makedirs(TweetDB.dbFolder)
            
        self.__dbConnection = sqlite3.connect(TweetDB.dbFolder + twitterHandle + TweetDB.dbFileExtension)
        self.__dbCursor = self.__dbConnection.cursor()
        
        self.__dbCursor.execute("""CREATE TABLE IF NOT EXISTS UserTimeline(id INTEGER UNIQUE, created_at TIMESTAMP, text VARCHAR(140), scrapped_at TIMESTAMP)""")
        self.commit()
        
    def insertRow(self, rowTuple):
        '''Insert row method

        ***Note***
        This method DOES NOT commit to the database automatically. You MUST commit using the commit() method after the
        insertRow() method is called (after each call or in batches after several insertRow calls.

        --args--
            rowTuple: list in the format (id INTEGER UNIQUE, created_at TIMESTAMP, text VARCHAR(140), scrapped_at TIMESTAMP)
        '''

        # rowTuple = (id INTEGER UNIQUE, created_at TIMESTAMP, text VARCHAR(140), scrapped_at TIMESTAMP)
        self.__dbCursor.execute('INSERT OR IGNORE INTO UserTimeline VALUES (?,?,?,?)', (rowTuple[0], rowTuple[1], rowTuple[2], rowTuple[3]))

    def commit(self):
        self.__dbConnection.commit()

    def __del__(self):
        self.__dbConnection.close()
