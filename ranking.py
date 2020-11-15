import query
import document_scoring
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class Ranking:
    def __init__(self, q):
        self.query = query.Query(q)
        '''
        Query Object
        '''
        self.similarity_scores = []
        '''
        Document - Query Cosine Similarity Scores
        '''
        self.document_ranking = []
        '''
        List of Doc Ids based on similarity score ranking
        '''

    def get_similarity_scores(self):
        '''
        Returns list of Document - Query Cosine Similarity Scores
        '''
        return self.similarity_scores
    
    def compute_similarity_score(self):
        '''
        Computes Document - Query Cosine Similarity Scores
        '''
        self.query.compute_query_score()
        query_vector = self.query.get_query_vector()
        doc_vectors = self.query.get_doc_vectors()

        for i in range(len(doc_vectors)):
            doc_vector = doc_vectors[i]
            similarity = cosine_similarity([doc_vector], [query_vector])
            self.similarity_scores.append(similarity[0][0])
            
    def document_ranking(self):
        '''
        Calculates Document Ranking based on Document - Query Cosine Similarity Scores
        '''
        s = numpy.array(self.similarity_scores) 
        sort_document = np.argsort(s)
        sort_document = [x + 1 for x in sort_document]
        self.document_ranking = sort_document[::-1]

    def get_doc_by_ranking(self):
        '''
        Prints top 10 Relevant Documents
        '''
        corpus = self.query.get_doc_content()
        print(corpus[0])
        for i in range(10):
            print('\n Document No ',i+1,'\n')
            print(corpus[self.document_ranking[i]])

if __name__ == "__main__":
    ranking = Ranking(['India','girl','education'])
    ranking.get_doc_by_ranking()
            
            
            
        
        
    
    
