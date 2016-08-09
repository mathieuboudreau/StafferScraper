import unittest
from stafferscraper.io.loadconfig import load_config

class LoadConfigTest(unittest.TestCase):
    
    def setUp(self):
        self.nonExistingFileName = '*WRONGF1LENAME.1X5!'
        
    def tearDown(self):
        pass
    
    def test_that_non_existing_filename_throws_error(self):
        self.assertRaises(FileNotFoundError, load_config, self.nonExistingFileName)
