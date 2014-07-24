#Noah Rubin
#06/26/2014
#Flaskr_blogapp.py

#import necessary libraries and methods
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify, request, make_response
import jieba
import json
import urllib2
from updatedCities import citiesDict, getCitiesHTML, parseCitiesWhile
import chardet

#from separate modules
from jiebaWebAPI_db import *
from jiebaWebAPI_process import *
from jiebaWebAPI_search import *

#From Miguel Gringberg
from requests.auth import HTTPBasicAuth

#Launch  "cronjob" python function to retreive updated cities list
getCitiesHTML()
parseCitiesWhile()

"""pragma mark createApp"""

#create the application and configure - note for bigger applications, configuration should be done in separate module
app = Flask(__name__)
app.config.from_object(__name__)
"""For verification: but have not gotten working yet
#auth = HTTPBasicAuth()"""

app.config.update(dict(DATABASE = os.path.join(app.root_path, 'flaskr.db'), DEBUG = False, SECRET_KEY = 'baixing_jieba'))
app.config.from_envvar('FLASKR_SETTINGS', silent = True)

#config object like a dictionary, can add new values like a dic
#app.rooth_path attribute used to find the path of the app, useful to maintain concurrency safe code
#environment specific configuration files advised, so can use from_envvar(). Define FLASKR_SETTINGS var that points to config file to be loaded. Silent says don't complain if no var exists
#can also use from_object() and config object from module provided will be loaded. Only uppercase var names included
#SECRET_KEY is to keep client-side sessions secure.  Make complex and hard to guess

"""HAVE NOT GOTTEN TO WORK YET
@auth.get_password
def get_password(username):
	if username == 'jieba':
		return 'baixing'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
	# return 403 instead of 401 to prevent browsers from displaying the default auth dialog
"""

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







