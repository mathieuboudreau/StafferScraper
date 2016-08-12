import unittest
import shutil
import os
import sqlite3
from stafferscraper.tweetdb import TweetDB

class TweetDatabaseTest(unittest.TestCase):
    
    testDatabaseFolder = '_database_test/'
    
    def setUp(self):
        self.oldDatabaseFolder  = TweetDB.dbFolder   # Save class default value
        TweetDB.dbFolder        = '_database_test/'
        self.TwitterHandle      = '_twitter_handle_test'

    def test_that_new_databse_folder_and_file_is_created_correctly(self):
        
        if os.path.exists('_database_test/'):
            print('Unit Test: Test database folder must not pre-exist')
            assert False # Test database folder must not pre-exist
        else:       
            testDB = TweetDB(self.TwitterHandle)
            assert os.path.isfile('_database_test/_twitter_handle_test' + TweetDB.dbFileExtension)
            del testDB
            
    def test_that_class_created_correct_database_table_columns_and_correct_order(self):
        testDB = TweetDB(self.TwitterHandle)
        
        connection = sqlite3.connect(TweetDB.dbFolder + self.TwitterHandle + TweetDB.dbFileExtension)
        cursor = connection.execute('select * from UserTimeline') # UserTimeline should be the hardcoded table name
        columnList = [description[0] for description in cursor.description] # get list of column names
        
        self.assertEqual(columnList, ['id', 'created_at', 'text'])
        
        del testDB

    def tearDown(self):
        if os.path.exists(TweetDatabaseTest.testDatabaseFolder):
            shutil.rmtree(TweetDatabaseTest.testDatabaseFolder)
            print('deleting test folder: ' + TweetDatabaseTest.testDatabaseFolder)
            
        TweetDB.dbFolder = self.oldDatabaseFolder # Return to class default
