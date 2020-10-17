from preprocessing import text_cleaning
import os


class BuildIndex:
    '''
    Builds Positional Inverted Index.
    '''
    
    def __init__(self):
        self.docID_doc = {}
        '''
        Dictionary of the form {docID:'filename'}.
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
        Dictionary of the form
        '''

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
        docs = os.listdir('data/bihar')
        for doc in docs:
            print(doc)
            file_extension = doc[-3:]
            if file_extension == 'txt':
                filename = 'data/all/' + doc
                f = open(filename, 'r', encoding="utf-8")
                self.create_docID_doc(i.docID, doc)
                content = text_cleaning(f)
                self.update_vocabulary(content)
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
                        inverted_pos_index[word][filename].extend(
                            doc_posIndex[filename][word][:])
                    else:
                        inverted_pos_index[word][filename] = doc_posIndex[filename][word]
                else:
                    inverted_pos_index[word] = {
                        filename: doc_posIndex[filename][word]}
        return inverted_pos_index


i = BuildIndex()

i.create_docID_content()
k = i.create_inverted_index()
