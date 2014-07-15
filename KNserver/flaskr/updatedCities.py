import urllib2

def getCitiesHTML():
	url = "http://baixing.com/?changeLocation=yes"    
	html = urllib2.urlopen(url)    
	myFile = open("Baixing_citySourceCode.txt", "w")
	for line in html:
		myFile.write(line)
	myFile.close

def parseCities():
	citiesDict = {}  #pinyin : char
	content = ""
	myFile = open("Baixing_citySourceCode.txt", "r")
	for line in myFile:
		content += line

	start = content.find("new_cities")
	end = content.find("</tr></table></table>")
	citiesPortion = content[start : end]
	pinStart = citiesPortion.find("://") + 3
	firstCityPortion = citiesPortion[pinStart: ] #reduces each iteration of below "for" loop

	pinCity = ""
	charCity = ""
	newCycleStart = 0

	for c in firstCityPortion :
		if c != "." :
			pinCity += c
		else : 
			pinCityEnd = firstCityPortion.find(c) #c=".", index relative to start of pin city name
			charStart = pinCityEnd + 15
			for z in firstCityPortion[15: ] :
				if z != "<" :
					charCity += z
				else :
					charCityEnd = firstCityPortion.find(z) #z="<", index relative to start pin city name
					newCycleStart = charCityEnd + 20
					break

			citiesDict[pinCity] = charCity
			pinCity = ""
			charCity = ""

			try: 
				firstCityPortion = firstCityPortion[charCityEnd + 20]  #can you change what you're "for"-ing over from within the for loop?
																#this is where you reduce (start later) firstCityPortion
			except IndexError:  #only happens once all cities exhausted
				break
					
	parsedCitiesFile = open("Parsed_Cities.txt", "w")
	parsedCitiesFile.write(str(citiesDict))
	parsedCitiesFile.close()

def parseCitiesWhile():
	# Parse source code file to get content
	citiesDict = {}  #pinyin : char
	content = ""
	myFile = open("Baixing_citySourceCode.txt", "r")
	for line in myFile:
		content += line
	myFile.close()

	# Cut content to only include table containing cities
	begin = content.find("new_cities")
	end = content.find("</tr></table></table>")
	content = content[begin:end]

	parsedCitiesFile = open('Parsed_Cities.txt', "w")

	# While loop to add cities pinyin and char to citiesDict
	while (len(content) > 0):
		pinStart = content.find("://")
		if (pinStart == -1):
			content = ""
		else:
			pinEnd = content.find(".")
			pinCity = content[pinStart + 3:pinEnd]

			charStart = pinEnd + 15
			charEnd = content.find("</a>")
			charCity = content[charStart:charEnd]

			citiesDict[pinCity] = charCity
			parsedCitiesFile.write(str(citiesDict[pinCity]))
			content = content[charEnd + 4:]

	parsedCitiesFile.close()

