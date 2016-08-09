import unittest
from stafferscraper.io.loadconfig import load_config

class LoadConfigTest(unittest.TestCase):
    
    def setUp(self):
        self.nonExistingFileName = '*WRONGF1LENAME.1X5!'
        self.requiredConfigFile  = 'config.yml'
        
    def tearDown(self):
        pass
    
    def test_that_non_existing_filename_throws_error(self):
        self.assertRaises(FileNotFoundError, load_config, self.nonExistingFileName)

    def test_that_ensures_config_file_exists(self):
        'If this test fails, config.yml.example should be renamed to config.yml and filled out'
        try:
            load_config(self.requiredConfigFile)
        except FileNotFoundError as e:
            assert False