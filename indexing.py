from preprocessing import text_cleaning
import os


class BuildIndex:
    '''
    Builds Positional Inverted Index.
    '''
    print('indexing')
    def __init__(self):
        self.docID_doc = {}
        '''
        Dictionary of the form {docID:'filename'}.
        '''
        self.doc_content = []
        '''
        List of Documents Content
        '''
        self.docID_content = {}
        '''
        Dictionary of the form {docID:[term1,term2,...]}.
        '''
        self.docID = 1
        '''
        ID Assigned to a document.
        '''
        self.vocabulary = set()
        '''
        Set of Unique Terms in the Corpus.
        '''
        self.inverted_pos_index = {}
        '''
        Dictionary of the form {term: {docID: [posIndex1, posIndex2]}, ...}, ...}
        '''
        self.tfidf = {}

    def get_no_of_doc(self):
        '''
        Returns no of Documents in the Corpus.
        '''
        return self.docID

    def get_inverted_pos_index(self):
        '''
        Returns inverted index of the corpus.
        Output: {term: {docID: [posIndex1, posIndex2]}, ...}, ...}
        '''
        return self.inverted_pos_index

    def get_vocabulary(self):
        '''
        Returns set of Unique terms in the Corpus.
        '''
        return self.vocabulary

    def update_vocabulary(self, content):
        '''
        Updates the Vocabulary Set.
        '''
        for word in content:
            self.vocabulary.add(word)

    def create_docID_doc(self, doc_ID, doc):
        '''
        Builds docID-docFileName dictionary.
        '''
        self.docID_doc[doc_ID] = doc

    def create_docID_content(self):
        '''
        Process documents, cleans them and builds docID_content dictionary
        '''
        docs = os.listdir('data/bihar')
        for doc in docs:
            print(doc)
            file_extension = doc[-3:]
            if file_extension == 'txt':
                filename = 'data/bihar/' + doc
                f = open(filename, 'r', encoding="utf-8")
                self.create_docID_doc(self.docID, doc)
                content = text_cleaning(f)
                self.doc_content.append(' '.join(content))
                self.update_vocabulary(content)
                self.docID_content[self.docID] = content
                self.docID += 1

    def create_inverted_index(self):
        '''
        Builds inverted index
        Output: {term: {docID: [posIndex1, posIndex2]}, ...}, ...}
        '''
        doc_posIndex = {}
        '''
        Dictionary of the form {docID: {term: [posIndex1, posIndex2, ...], ... }}
        '''
        for id in self.docID_content:
            content = self.docID_content[id]
            doc_index = {}
            for index, word in enumerate(content):
                if word in doc_index.keys():
                    doc_index[word].append(index)
                else:
                    doc_index[word] = [index]
            doc_posIndex[id] = doc_index

        for id in doc_posIndex.keys():
            for word in doc_posIndex[id].keys():
                if word in self.inverted_pos_index.keys():
                    if id in self.inverted_pos_index[word].keys():
                        self.inverted_pos_index[word][id].extend(doc_posIndex[id][word][:])
                    else:
                        self.inverted_pos_index[word][id] = doc_posIndex[id][word]
                else:
                    self.inverted_pos_index[word] = {id: doc_posIndex[id][word]}
            
    def execute(self):
        '''
        Driver function
        '''
        
        self.create_docID_content() 
        self.create_inverted_index()

if __name__ == "__main__":
    index = BuildIndex()
    index.execute()
