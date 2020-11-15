import indexing
from sklearn.feature_extraction.text import TfidfVectorizer

class DocScore:

    def __init__(self):
        print('doc score')
        self.index = indexing.BuildIndex()
        '''
        Index Object
        '''
        self.corpus = []
        '''
        List of Documents Content
        '''
        self.terms = []
        '''
        Vocabulary
        '''
        self.term_idf = {}
        '''
        Dictionary of terms and their inverse document frequency
        '''
        self.doc_tfidf = 0
        '''
        Document-Term TF-IDF matrix
        '''

    def get_terms(self):
        '''
        Returns list of vocabulary
        '''
        return self.terms

    def get_term_idf(self):
        '''
        Returns dictionary of terms and their inverse document frequency
        '''
        return self.term_idf

    def get_doc_tfidf(self):
        '''
        Returns matrix of Document-Term TF-IDF
        '''
        return self.doc_tfidf
        
    def compute_doc_score(self):
        '''
        Computes Document - Term TF-IDF Matrix
        '''
        self.index.execute()
        self.corpus = self.index.doc_content
        vectorizer = TfidfVectorizer()
        self.doc_tfidf = vectorizer.fit_transform(self.corpus)
        self.doc_tfidf = self.doc_tfidf.toarray()
        self.terms = vectorizer.get_feature_names()
        self.term_idf = dict(zip(vectorizer.get_feature_names(), vectorizer.idf_))
        
if __name__ == "__main__":
    s = DocScore()
    s.compute_doc_score()
        
