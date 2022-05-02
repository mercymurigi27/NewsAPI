
from flask import render_template, request, redirect, url_for
from ..request import get_sources, get_articles
from . import main



@main.route("/")
def index():
    """
    Views root page  function and returns data
    """

    title = 'Home - Welcome to News App'

    source = get_sources()
    
    return render_template("index.html", title = title, source = source)    

