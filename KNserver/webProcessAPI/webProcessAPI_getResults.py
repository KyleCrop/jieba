#This file uses the encoding: utf-8
#08/01/2014
#Noah Rubin
#getSearchResults.py

from requests import get, put
from requests.auth import HTTPBasicAuth
from urllib import quote_plus
from urllib2 import urlopen

inquiry = '婴儿床'.decode('utf-8')

''' pragma mark Extract relevant corpuses 

def extractCorpuses(inquiry):
	"""Returns: list of corpuses from top 5 relevant results
	based on user inquiry
	Precondition: inquiry is str with UTF-8 encoding"""
	rawCorpuses = []
	#TO-DO
	return rawCorpuses '''

def Main():
	query = get('http://www.ask.com/web?q=' + quote_plus(inquiry.encode('utf-8')) + 'site:sh.58.com')
	print query.headers
	print query.apparent_encoding
	print query.encoding
	print query.text
	# find helpful resources and parse those links, not relevant adds
