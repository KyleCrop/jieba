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
	results = {}
	for corpus in corpusList:
		keywords = jieba.analyse.extract_tags_withFrequency(corpus,15)
		for keyword in keywords:
			results[keyword[1]] = results.get(keyword[1],0.0)+keyword[0]
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
	resultsCopy = results
	for keyword in resultsCopy:
		times_in = 0
		for word in inquiry:
			if word in keyword[0]:
				times_in += 1
		if times_in == 0:
			resultsCopy.remove(keyword)
	return resultsCopy




