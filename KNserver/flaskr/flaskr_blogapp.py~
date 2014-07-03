#Noah Rubin
#06/26/2014
#Flaskr_blogapp.py

#import necessary libraries and methods
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import jieba

"""pragma mark createApp"""

#create the application and configure - note for bigger applications, configuration should be done in separate module
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE = os.path.join(app.root_path, 'flaskr.db'), DEBUG = True, SECRET_KEY = 'development key', USERNAME = 'admin', PASSWORD = 'default'))
app.config.from_envvar('FLASKR_SETTINGS', silent = True)

#config object like a dictionary, can add new values like a dic
#app.rooth_path attribute used to find the path of the app, useful to maintain concurrency safe code
#environment specific configuration files advised, so can use from_envvar(). Define FLASKR_SETTINGS var that points to config file to be loaded. Silent says don't complain if no var exists
#can also use from_object() and config object from module provided will be loaded. Only uppercase var names included
#SECRET_KEY is to keep client-side sessions secure.  Make complex and hard to guess

"""pragma mark databaseAndApplicationContext"""

#opening connection to the specified database.  Makes ______ easier.
def connect_db():
	"""Connects to the specific database created for app
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

@app.teardown_appcontext #app context created before request and torn down after request
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

"""pragma mark viewFunction"""

@app.route('/')
def show_entries():
	"""Shows entries in the database"""
	db = get_db()
	cur = db.execute('select proc, text from entries order by id desc')
	entries = cur.fetchall()
	return render_template('show_entries.html', entries=entries)

@app.route('/add', methods = ['POST'])
def add_entry():
	"""Adds an entry to the database"""
	if not session.get('logged_in'):
		abort(401)
	db = get_db()
	seg_list = jieba.cut_for_search(request.form['text'])
	output = "  ".join(seg_list)
	db.execute('insert into entries (text, proc) values (?,?)', [request.form['text'], output])
	db.commit()
	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	"""Login protocol"""
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('show_entries'))
	return render_template('login.html', error = error)

@app.route('/logout')
def logout():
	"""Logout protocol"""
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('login'))


if __name__ == '__main__':
	app.run(host="0.0.0.0")






