import unittest, shutil, os
import sqlite3
from stafferscraper.tweetdb import TweetDB

class TweetDatabaseTest(unittest.TestCase):
    
    testDatabaseFolder = '_database_test/'
    
    def setUp(self):
        self.oldDatabaseFolder  = TweetDB.dbFolder   # Save class default value
        TweetDB.dbFolder        = '_database_test/'
        self.TwitterHandle      = '_twitter_handle_test'
        self.sample_row         = (90000014,'2010-04-09T12:53:54','This is a tweet!','2016-08-20T03:12:45')

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

        self.assertEqual(columnList, ['id', 'created_at', 'text', 'scrapped_at'])

        del testDB

    def test_that_insert_method_commits_changes_to_db_and_db_row_matches_insert_arg(self):
        testDB = TweetDB(self.TwitterHandle)
        testDB.insertRow(self.sample_row)
        
        connection = sqlite3.connect(TweetDB.dbFolder + self.TwitterHandle + TweetDB.dbFileExtension)
        cursor = connection.execute('SELECT * FROM UserTimeline ORDER BY id ASC LIMIT 1') # UserTimeline should be the hardcoded table name
        columnList = cursor.fetchone() # get list of column names

        self.assertEqual(columnList, self.sample_row)
        
        del testDB

    def tearDown(self):
        if os.path.exists(TweetDatabaseTest.testDatabaseFolder):
            shutil.rmtree(TweetDatabaseTest.testDatabaseFolder)

        TweetDB.dbFolder = self.oldDatabaseFolder # Return to class default
