#This file uses the encoding: utf-8
#07/31/2014
#Noah Rubin
#processSearchResults.py

import jieba
import jieba.analyse

''' pragma mark Format user inquiry '''

def constructArray(sentence,delimiter=' '):
	"""Returns: array of objects separated by delimiter (defaults to one white space)

		
		Example: constructArray('I love cheese', ' ') --> ['I', 'love', 'cheese']

	Preconditions: sentence and delimiter are of type str"""
	inquiryList = sentence.split(delimiter)
	return set(inquiryList)

''' pragma mark Extract result keywords '''

def buildResultDict(corpusList):
	"""Returns: Dictionary of all keywords and frequencies extracted from
	the five corpuses without duplicates, format: {keyword : frequency}

		Note: If duplicate word is found, frequency of word is added
		to frequency already in dictionary

		Format: {keyword : total frequency}

	Precondition: resultList is a list of 5 strings"""
	assert len(corpusList) <= 5, 'list has more than 5 elements'
	results = {}
	for corpus in corpusList:
		keywords = jieba.analyse.extract_tags_withFrequency(corpus,15)
		for keyword in keywords:
			results[keyword[1]] = results.get(keyword[1],0.0)+keyword[0]
	return results

''' pragma mark Determine most comprehensive result'''

def compareKeywords(inquiryList, results, topK = 6):
	"""Returns: List of tuples containing top topK highest frequency
	words that have at least one character in common with inquiry

		Example: If inquiry contains "床," then "婴儿床" would be
		passible with high enough frequency

		Note: The speed of this algorithm is heavily dependent on
		the length of user inquiry. Speed is proportional to number
		of words in inquiry and number of keywords (max distinct 75)

	Precondition: inquiryList is a string list, results is dictionary"""
	resultsCopy = set([]) #maintain integrity of results data
	for key in results:
		for word in inquiryList:
			if word in key:
				print "found a match"
				newTuple = (key,results.get(key,0.0))
				resultsCopy.add(newTuple)
	resultsCopy = list(resultsCopy)
	resultsCopy = sorted(resultsCopy, key = _getKey, reverse=True)
	return resultsCopy[:topK]

def _getKey(item):
	"""Helper method for compareKeywords
	Returns: Key of tuple to be used for sorting"""
	return item[1]




