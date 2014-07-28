#necessary imports
import os
import sqlite3
from flask import Flask, g

#create the application and configure - note for bigger applications, configuration should be done in separate module
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE = os.path.join(app.root_path, 'flaskr.db'), DEBUG = True, SECRET_KEY = 'baixing_jieba'))
app.config.from_envvar('FLASKR_SETTINGS', silent = True)

def connect_db():
	"""Connects to the database
	Uses sqlite3.Row object to represent rows - treat rows
	as dictionaries rather than tuples"""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

def get_db():
	"""Opens a new database connection if there is not one open yet for 
	current application context"""
	if not hasattr(g,'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

def close_db(error):
	"""Closes the database again at the end of request
	Tears down the app """
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

def init_db(): 
	"""Creates the application context before request is sent
	Without application context, g object (where store information) does
	now know which context to become"""
	with app.app_context(): #establishes application context
		db = get_db() 
		with app.open_resource('schema.sql', mode = 'r') as f: #opens resource provided by app
			db.cursor().executescript(f.read()) #executes the schema.sql script to create database
		db.commit() #commit the changes -- teardown functions executed afterward







