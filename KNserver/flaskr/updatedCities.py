import urllib2

def getCitiesHTML():
	url = "http://baixing.com/?changeLocation=yes"    
	html = urllib2.urlopen(url)    
	myFile = open("Baixing_citySourceCode.txt", "w")
	for line in html:
		myFile.write(line)
	myFile.close
	
def parseCities():
	cities = {}  #pinyin : char
	content = ""
	myFile = open("Baixing_citySourceCode.txt", "r")
	for line in myFile:
		content += line
	
	start = content.find("new_cities")
	stuff = content[start : content.find("</tr></table></table>")]
	
	
