from sklearn.feature_extraction.text import TfidfVectorizer

def get_tfidf_matrix(sentences):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)
    return X.toarray(), vectorizer