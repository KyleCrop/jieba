#This file uses the encoding: utf-8
#08/01/2014
#Noah Rubin
#processResultsTest.py

from processSearchResults import *

#Set up test raw corpus list
rawCorpuses = []
rawCorpuses.append('高英、袁殿华、曹迎军、倪振娥、曾淑煌、张秀桃、王建、罗大富、许绍坤、巴依卡•凯力迪别克等10名“最美拥军人物”来自不同地区'.decode('utf-8'))
rawCorpuses.append('这下就成不折不扣的神经城市了。进城后的农户就是将农村土地挖地三尺也不知能坚持在城里生活多少个年月。'.decode('utf-8'))
rawCorpuses.append('8月1日拍摄的台湾高雄前镇爆炸事故现场。 7月31日晚，高雄市前镇区多条街道陆续发生可燃气体外泄，并引发多次大爆炸，数条街道被波及'.decode('utf-8'))
rawCorpuses.append('7月17日下午，甘肃酒泉市政府办公室对外发布消息披露：“7月16 日，甘肃省玉门市发现一例鼠疫病例致1人死亡，目前死者遗体已按有关规范进行妥善处理'.decode('utf-8'))
rawCorpuses.append('清凉小学，是安徽省蚌埠市固镇县的一所乡村小学。几年前，有人捐助了20万元为学校盖了栋三层教学楼，至今仍是村子里最高的建筑。摄影师用一年时间)'.decode('utf-8'))

#Set up test user inquiry - rigged such that last corpus should be most relevant
inquiry = '清凉小学几年前至今仍是村子里最高的建筑'.decode('utf-8')
inquiryCut = jieba.cut(inquiry)
inquiryCutStr = " | ".join(inquiry)
inquiryList = constructArray(inquiryCutStr,' | ')

def Main():
	results = buildResultDict(rawCorpuses)
	for key in results:
		print key
	print "-----> now comparing keywords"
	for word in inquiryList:
		print word
	keywordSet = compareKeywords(inquiryList,results)
	print "-----> now print keywordSet "
	for item in keywordSet:
		print item[0] + str(item[1])
