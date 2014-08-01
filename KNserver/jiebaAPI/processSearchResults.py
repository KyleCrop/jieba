#07/31/2014
#Noah Rubin
#processSearchResults.py

import jieba
import jieba.analyse

''' pragma mark Format user inquiry '''

#used to construct array from user inquiry
def constructArray(sentence,delimiter=' '):
	"""Returns: array of objects separated by delimiter (defaults to one white space)
	Example: constructArray('I love cheese', ' ') --> ['I', 'love', 'cheese']
	Preconditions: sentence and delimiter are of type str"""
	return sentence.split(delimiter)

''' pragma mark Extract result keywords '''

def buildResultList(corpusList):
	"""Returns: list of Result objects with keywords extracted from 
	corpus and set in keywords attribute
	Precondition: resultList is a list of 5 strings"""
	assert len(corpusList) <= 5, 'list has more than 5 elements'
	results = []
	for corpusStr in corpusList:
		results.append(Result(corpusStr))
	#extract keywords from corpuses - topK set to 15
	for result in results:
		result.setKeywords(jieba.analyse.extract_tags(result.corpus,15))
	return results

''' pragma mark Determine most relevant link'''

def compareKeywords(inquiryList, results):
	"""Returns: corpus with largest relevancy count
	Note: relevancy is calculated as # of keywords in common
	with words in the user inquiry
	Precondition: inquiryList is a string list, result is a list
	of Result objects with non-empy keywords lists and relevancy
	set to 0"""
	maxRelevancy = 0
	finalCorpus = ''
	for result in results:
		for word in inquiryList:
			if word in result.getKeywords():
				result.incrementRel()
		if result.getRelevancy() > maxRelevancy:
			finalCorpus = result.getCorpus()
	return finalCorpus

''' pragma mark Result Class '''

class Result(object):
	"""Each instance is corpus from search result, relevancy information,
	and a list of keywords"""

#constructor
	def __init__(self,corpusStr):
		"""Constructor for Result object
		Returns: Link object with attributes corpus (str),
		relevancy (int) initially set to 0, and keywords (list of str)
		Precondition: corpus is of type str"""
		super(Result, self).__init__()
		corpus = corpusStr
		relevancy = 0
		keywords = []

#getters
	def getCorpus(self):
		"""Getter for url"""
		return corpus

	def getRelevancy(self):
		"""Getter for relevancy"""
		return relevancy

	def getKeywords(self):
		"""Getter for keywords list"""
		return keywords

#setters
	def setKeywords(self,keywordList):
		"""Setter fro keywords list"""
		keywords = keywordList

#methods
	def incrementRel(self):
		"""Procedure: increment relevancy attr"""
		relevancy += 1

