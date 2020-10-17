from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re


def text_cleaning(file):
    '''
    Cleans the Document Content.
    Removes stopwords,
    lemmatize the terms,
    Removes non-alphanumeric terms,
    Convertes to lower case
    '''
    stop_words = stopwords.words('english')
    lemmatizer = WordNetLemmatizer()
    content = []
    for line in file:
        terms = line.strip()
        terms = re.sub('[^0-9a-zA-Z]+', ' ', terms)
        term_list = terms.split(' ')
        for word in term_list:
            content.append(word)

    preprocessed_content = []
    for word in content:
        word = word.lower()
        if word and word not in stop_words:
            word = lemmatizer.lemmatize(word)
            preprocessed_content.append(word)
    return preprocessed_content
