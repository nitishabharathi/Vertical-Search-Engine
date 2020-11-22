import document_scoring
from collections import Counter
import numpy as np

class Query:
    def  __init__(self, query):
        print('query')
        self.query = query
        '''
        Query String
        '''
        self.query_vector = []
        '''
        Query TF-IDF Vector
        '''
        self.doc_score = document_scoring.DocScore()
        '''
        Document Score Object
        '''
        
    def get_query_vector(self):
        '''
        Returns Query TF-IDF Vector
        '''
        return self.query_vector

    def get_doc_vectors(self):
        '''
        Returns Document-Term TF-IDF matrix
        '''
        return self.doc_score.get_doc_tfidf()
    
    def get_doc_content(self):
        '''
        Returns List of Documents Content
        '''
        return self.doc_score.corpus
    
    def compute_query_score(self):
        '''
        Computes Query TF-IDF Vector
        '''
        self.doc_score.compute_doc_score()
        terms = self.doc_score.get_terms()
        term_idf = self.doc_score.get_term_idf()
        query_term_frequency = dict(Counter(self.query))

        query_tfidf = {}
        for term in query_term_frequency.keys():
            try:
                query_tfidf[term] = query_term_frequency[term]*term_idf[term]
            except:
                continue
        self.query_vector = np.zeros(len(terms))

        for term in self.query:
            try: 
                term_index = terms.index(term)
                query_vector[term_index] = query_tfidf[term]
            except:
                continue
        #return doc_score,query_vector
            
        
        
        
        
