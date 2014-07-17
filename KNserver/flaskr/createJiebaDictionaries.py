import os
from datetime import datetime
import icu

cities = []
"""THIS IS THE LINE THAT GRABS THE CITY NAMES, DON'T UNCOMMENT OR RISK CREATING 4037 FILES"""
#parsedCities = open("Parsed_Cities.txt", "r")

for line in parsedCities :
	stopAt = line.find(":")
	cities.append(line[:stopAt])
parsedCities.close()

dictionary = ""
jiebaDict = open("dict.txt", "r")
for line in jiebaDict :
	dictionary += line

#Hard-coding categories because assuming they'll stay constant	
categories = ["ershou", "qiuzhi", "cheliang", "jianzhi", "fangwu", "jiaoyou", "chongwu", "zhaopin", "fuwu", "jianliku", "peixun"]

#For speed-testing
timeA = datetime.now()
print timeA

#NEED TO SPECIFY ENTIRE PATH FROM ROOT, so change 'kyle' to whatever necessary
for city in cities :
	path = "/home/kyle/Documents/jieba/KNserver/flaskr/dictionaries/" + city
	os.mkdir(path)
	
	"""
	Need to make directories within this directory for each city,
	put each dictionary into the correct /dictionaries/city directory.
	Also test that parsing "city" works (Shanghai:2i3422uih3)
	"""
	
	for category in categories :
		fileName = "/home/kyle/Documents/jieba/KNserver/flaskr/dictionaries/" + city + "/" + city + "_" + category
		newDict = open(fileName, "w")
		newDict.write(dictionary)
		newDict.close()

#For speed-testing
timeB = datetime.now()
print timeB

timeE = timeB - timeA
print timeE.seconds
