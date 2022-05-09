import unittest
from app.models import Article, Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("abc-news","ABC News","Lorem10","en")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_source.id, "abc-news")
        self.assertEqual(self.new_source.name, "ABC News")
        self.assertEqual(self.new_source.desc, "Lorem10")
        self.assertEqual(self.new_source.lang, "en")

       