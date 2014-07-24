#Noah Rubin
#06/26/2014
#Flaskr_blogapp.py

#import necessary libraries and methods
from flask import session, g, abort, request, make_response
from updatedCities import citiesDict, getCitiesHTML, parseCitiesWhile
from jiebaWebAPI_search import *

#Launch  "cronjob" python function to retreive updated cities list
getCitiesHTML()
parseCitiesWhile()

"""pragma mark createApp"""

#create the application and configure - note for bigger applications, configuration should be done in separate module
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE = os.path.join(app.root_path, 'flaskr.db'), DEBUG = False, SECRET_KEY = 'baixing_jieba'))
app.config.from_envvar('FLASKR_SETTINGS', silent = True)

#SECRET_KEY is to keep client-side sessions secure.  Make complex and hard to guess

@app.errorhandler(400)
def not_found(error):
	return make_response(jsonify( { 'error': 'Bad request' } ), 400)
 
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify( { 'error': 'Not found' } ), 404)

"""pragma mark View Functionality"""

@app.route('/')
def model_show_entries():
	print "works up to here?"
	session.clear()
	return show_entries()

#Makes citiesDict available to all templates
#Keeping this function here because of global var inheritence
@app.context_processor
def inject_citiesDict():
	"""Passes the cities dictionary to application context"""
	global citiesDict
	return dict(citiesDict = citiesDict)

@app.route('/process', methods = ['POST'])
def model_process_words():
	return process_words()

@app.route('/addWords', methods = ['POST'])
def model_addToDictionary():
	return addToDictionary()
	
@app.route('/updateDictionary', methods = ['POST'])
def model_updateDictionary():
	return updateDictionary()

@app.route('/queryDictionary', methods = ['GET', 'POST'])
def model_queryDictionary():
	return queryDictionary()

@app.route('/sendQuery', methods = ['GET', 'POST'])
def model_sendQuery():
	return sendQuery()

''' pragma mark Helper Functions '''

def model_searchDictionary(dictionary, query):
	return _searchDictionary(dictionary, query)


if __name__ == '__main__':
	app.run(host="0.0.0.0")







