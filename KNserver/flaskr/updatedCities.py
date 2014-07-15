import urllib2

citiesDict = {}  #pinyin : char

def getCitiesHTML():
	url = "http://baixing.com/?changeLocation=yes"    
	html = urllib2.urlopen(url)    
	myFile = open("Baixing_citySourceCode.txt", "w")
	for line in html:
		myFile.write(line)
	myFile.close

def parseCitiesWhile():
	# Parse source code file to get content
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
			content = content[charEnd + 4:]

	parsedCitiesFile.write(str(citiesDict))
	parsedCitiesFile.close()

