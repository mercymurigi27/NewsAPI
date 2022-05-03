from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_O_four(error):
  '''
  function to run 404 page
  '''
  return render_template('four_Ow_four.html'),404