#necessary imports
from jiebaWebAPI_process import *
import chardet

def queryDictionary():
	"""Adds queried word to session dictionary and renders the
	query dictionary page"""
	try:
		queriedWord = session['queriedWord'].decode('utf-8')
		queriedWordFrequency = session['queriedWordFrequency'].decode('utf-8')
	except:
		queriedWord = ''
		queriedWordFrequency = ''
	return render_template('Query_Dictionary.html', queriedWord=queriedWord, queriedWordFrequency=queriedWordFrequency)

def sendQuery():
	"""Processes user query and sets session vars for word and frequency.
	Values are accessed with keys queriedWord and queriedWordFrequency"""
	query = request.form.get('query') #might have to fix encoding, keep in mind! look for decoding error
	dictionary = open(jieba.get_abs_path_dict())
	dictArray = _searchDictionary(dictionary, query)
	try:
		session['queriedWord'] = dictArray[0]
		session['queriedWordFrequency'] = dictArray[1]
	except:
		print "Not found"
	return redirect(url_for('model_queryDictionary'))

def _searchDictionary(dictionary, query):
	"""Helper function: searches the dictionary text file for
	given query, returns array with format [word,frequency] or empty
	dictionary.  Note: if line has improper encoding will not be searched"""
	for line in dictionary:
		encodingDict = chardet.detect(line)
		print encodingDict
		encoding = encodingDict['encoding']
		try:
			line = unicode(line, encoding)
			if query in line:
				ind = line.find(' ')
				word = line[0:ind]
				if query == word:
					print "Found it"
					ind2 = line.rfind(' ')
					frequency = line[ind+1:ind2]
					return [word.encode('utf-8'),frequency.encode('utf-8')]
		except:
			print "I failed to decode: " + encoding
			pass
	return []

