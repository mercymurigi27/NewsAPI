import urllib.request,json
import datetime
from .models import Source, Article

# Getting api key
api_key = None
# Getting the source base url
base_url = None
# Getting the article base url
article_base_url = None


def configure_request(create_app):
    global api_key,base_url,article_base_url
    api_key = create_app.config['API_KEY']
    base_url = create_app.config['SOURCES_BASE_URL']
    article_base_url= create_app.config['ARTICLE_BASE_URL']

def get_sources():
    """
    gets Json response
    """
    get_source_url = base_url.format(api_key)
    
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        
        source_results = None
        
        if get_source_response["sources"]:
            source_results_list = get_source_response["sources"]
            source_results = process_results(source_results_list)
            
    return source_results      

def process_results(source_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    source_results = []


    for source_item in source_list:
            id = source_item.get("id")
            name = source_item.get("name")
            desc = source_item.get("description")
            lang = source_item.get("language")
            
            if lang == "en":
                source_object = Source(id, name, desc, lang)
                source_results.append(source_object)
                
    return source_results    

