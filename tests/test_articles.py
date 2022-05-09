import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("abc-news","ABC News","Lorem10","en")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_article.id, "abc-news")
        self.assertEqual(self.new_article.name, "ABC News")
        self.assertEqual(self.new_article.desc, "Lorem10")
        self.assertEqual(self.new_article.lang, "en")

       