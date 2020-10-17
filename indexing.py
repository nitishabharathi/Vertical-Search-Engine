import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re



import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import math
import pandas as pd





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



class BuildIndex:
    def __init__(self):
        self.docID_doc = {}
        self.docID_content = {}
        self.docID = 1
        self.vocabulary = set()
        self.inverted_pos_index = {}

    def updateVocabulary(self,content):
        for word in content:
            self.vocabulary.add(word)

    def create_docID_doc(self,doc_ID,doc):
        self.docID_doc[doc_ID] = doc

    def create_docID_content(self):
        docs = os.listdir('data/bihar')
        for doc in docs:
            print(doc)
            file_extension = doc[-3:]
            if file_extension == 'txt':
                filename = 'data/all/' + doc
                f = open(filename,'r',encoding="utf-8")
                #i.docID_doc[i.docID] = doc
                self.create_docID_doc(i.docID,doc)
                content = preprocess(f)
                self.updateVocabulary(content)
                self.docID_content[self.docID] = content
                self.docID += 1

    def create_inverted_index(self):
        doc_posIndex = {}
        for id in self.docID_content:
            content = self.docID_content[id]
            fileIndex = {}
            for index, word in enumerate(content):
                    if word in fileIndex.keys():
                            fileIndex[word].append(index)
                    else:
                            fileIndex[word] = [index]
            posIndex = fileIndex
            doc_posIndex[id] = posIndex

        inverted_pos_index = {}
        for filename in doc_posIndex.keys():
            for word in doc_posIndex[filename].keys():
                if word in inverted_pos_index.keys():
                    if filename in inverted_pos_index[word].keys():
                        inverted_pos_index[word][filename].extend(doc_posIndex[filename][word][:])
                    else:
                        inverted_pos_index[word][filename] = doc_posIndex[filename][word]
                else:
                    inverted_pos_index[word] = {filename: doc_posIndex[filename][word]}
        return inverted_pos_index


i = BuildIndex()
stop_words=stopwords.words('english')
ps = PorterStemmer()    

i.create_docID_content()
k = i.create_inverted_index()


























    


    
