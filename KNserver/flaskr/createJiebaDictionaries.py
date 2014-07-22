import os
from datetime import datetime
from chardet import detect

cities = []
"""THIS IS THE LINE THAT GRABS THE CITY NAMES, DON'T UNCOMMENT OR RISK CREATING 4037 FILES"""
#parsedCities = open("Parsed_Cities.txt", "r")

def createDicts() :
	for line in parsedCities :
		stopAt = line.find(":")
		cities.append(line[:stopAt])
	parsedCities.close()

	dictionary = ""
	jiebaDict = open("dict.txt", "r")
	for line in jiebaDict :
		dictionary += line

	# Hard-coding categories because assuming they'll stay constant	
	categories = ["ershou", "qiuzhi", "cheliang", "jianzhi", "fangwu", "jiaoyou", "chongwu", "zhaopin", "fuwu", "jianliku", "peixun"]

	"""
	#For speed-testing
	timeA = datetime.now()
	print timeA
	"""

	# Create "dictionaries" directory if not already created, NEED TO SPECIFY PATH FROM ROOT
	try: path = "/home/kyle/Documents/jieba/KNserver/flaskr/dictionaries"
		os.mkdir(path)
	except:
		pass

	# NEED TO SPECIFY ENTIRE PATH FROM ROOT, so change 'kyle' to whatever necessary
	for city in cities :
		path = "/home/kyle/Documents/jieba/KNserver/flaskr/dictionaries/" + city
		os.mkdir(path)
	
		"""
		Need to make to make a separate directory for each city within this directory
		put each dictionary into the correct /dictionaries/city directory.
		"""
	
		for category in categories :
			fileName = "/home/kyle/Documents/jieba/KNserver/flaskr/dictionaries/" + city + "/" + city + "_" + category
			newDict = open(fileName, "w")
			newDict.write(dictionary)
			newDict.close()

	"""
	#For speed-testing
	timeB = datetime.now()
	print timeB

	timeE = timeB - timeA
	print timeE.seconds
	"""


def makeUniform(originalDictPath,newDictPath):
	"""Procedure: Converts all entries, if possible, in given dictionary to
	UTF-8 encoding and writes to a new dictionary text file
	Precondition: originaldictPath && newDictPath must be full valid paths
	to dictionary text files"""
	otxtFile = open(originalDictPath)
	ntxtFile = open(newDictPath, 'w')
	for line in otxtFile:
		encodeDict = detect(line)
		encoding = encodeDict['encoding']
		if (encoding != 'utf-8'):
			try:
				line = unicode(line, encoding)
				#line = line.encode('utf-8')
				ntxtFile.write(line)
			except:
				print "Failed to re-encode line: " + line + "\n" + "with encoding " + encoding
				ntxtFile.write(line + "--re-encodeFail" + encoding)
	otxtFile.close()
	ntxtFile.close()
	print 'Process finished. Please review output for failed conversions.'
