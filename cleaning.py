
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import math
import pandas as pd


docs = os.listdir('data/bihar')
stop_words=stopwords.words('english')
ps = PorterStemmer()
docID_doc = {}
docID_content = {}
docID = 1
vocabulary = set()
print('hry')

def updateVocabulary(content):
    for word in content:
        vocabulary.add(word)


def preprocess(file):
    content = []
    for line in file:
        stripped_line = line.strip()
        stripped_line = re.sub('[^0-9a-zA-Z]+', ' ', stripped_line)
        line_list=stripped_line.split(' ')
        for word in line_list:
            content.append(word)
    preprocessed_content = []
    for word in content:
        word=word.lower()#normalising-lower
        if word and word not in stop_words:#removing empty strings and stop words
            word=ps.stem(word)#lemmatize
            preprocessed_content.append(word)
    return preprocessed_content

for doc in docs:
    print(doc)
    file_extension = doc[-3:]
    if file_extension == 'txt':
        filename = 'data/all/' + doc
        f = open(filename,'r',encoding="utf-8")
        docID_doc[docID] = doc
        
        content = preprocess(f)
        updateVocabulary(content)
        docID_content[docID] = content
        docID += 1

def index_one_file(termlist):
	fileIndex = {}
	for index, word in enumerate(termlist):
		if word in fileIndex.keys():
			fileIndex[word].append(index)
		else:
			fileIndex[word] = [index]
	return fileIndex
    
doc_posIndex = {}

for id in docID_content:
    content = docID_content[id]
    posIndex = index_one_file(content)
    doc_posIndex[id] = posIndex


#input = {filename: {word: [pos1, pos2, ...], ... }}
#res = {word: {filename: [pos1, pos2]}, ...}, ...}
def fullIndex(regdex):
	total_index = {}
	for filename in regdex.keys():
		for word in regdex[filename].keys():
			if word in total_index.keys():
				if filename in total_index[word].keys():
					total_index[word][filename].extend(regdex[filename][word][:])
				else:
					total_index[word][filename] = regdex[filename][word]
			else:
				total_index[word] = {filename: regdex[filename][word]}
	return total_index
final = fullIndex(doc_posIndex)
