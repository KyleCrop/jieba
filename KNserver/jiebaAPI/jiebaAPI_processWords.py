#Noah Rubin
#07/24/2014
#jiebaAPI_processWords.py

import jieba
import json

def processWords(sentence):
	"""Processes given input using Jieba cut method, SEO mode
	Returns: JSON representation of separated input
	Precondition: sentence is of type str"""
	seg_list = jieba.cut_for_search(sentence) #initializes trie
	output = " | ".join(seg_list)
	joutput = json.dumps(output)
	return joutput