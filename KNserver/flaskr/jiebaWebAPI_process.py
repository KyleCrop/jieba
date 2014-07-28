#necessary imports
from flask import Flask, redirect, url_for, render_template, flash, get_flashed_messages, request
import jieba
import json

#from separate modules
from jiebaWebAPI_init import *

def show_entries():
	"""Populates view with entries from database,
	passes entries to show_entries template and renders"""
	print "works inside show_entries?"
	db = get_db()
	print "2 works inside show_entries?"
	cur = db.execute('select proc, text from entries order by id desc') 
	latest = cur.fetchone()
	entries = cur.fetchall()
	return render_template('show_entries.html', latest=latest, entries=entries)

def process_words():
	"""Processes text input and JSON dumps entry to the database"""
	db = get_db()
	seg_list = jieba.cut_for_search(request.form['text']) #initializes trie
	output = " / ".join(seg_list)
	joutput = json.dumps(output)
	db.execute('insert into entries (text, proc) values (?,?)', [request.form['text'], joutput])
	db.commit()
	return redirect(url_for('model_show_entries'))

def addToDictionary():
	"""Grabs list of checked words and adds to the operating dictionary
	Note: If word already exists in dictionary, increments frequency"""
	wordList = request.form.get('segCheckbox')
	for word in wordList:
		jieba.add_word(word,1)
	flash("You successfully updated the dictionary!")
	return redirect(url_for('model_show_entries'))

def updateDictionary():
	"""Changes the operating dictionary based on user choice on web"""
	city = request.form.get("cityContainer")
	category = request.form.get("categoryContainer")
	#jieba.set_dictionary('/home/noah/jieba/KNserver/flaskr/jieba/dictionaries/%(cityVar)s/%(cityVar)s_%(categoryVar)s.txt' % \ {'cityVar':city, 'catVar':category})
	print "Operating dictionary is: " + str(jieba.get_abs_path_dict())
	return redirect(url_for('model_show_entries'))











