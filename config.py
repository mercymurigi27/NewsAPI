import os


class Config:
    '''
    General configuration parent class
    '''
    SOURCES_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    ARTICLE_BASE_URL = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"
    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')