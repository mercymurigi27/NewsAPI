class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,description,language):
        self.id =id
        self.name = name
        self.desc = description
        self.lang = language




class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,urlToImage, title, description,url, publishedAt, source):
        self.image = urlToImage
        self.title = title
        self.desc = description
        self.url = url
        self.time = publishedAt
        self.source = source
