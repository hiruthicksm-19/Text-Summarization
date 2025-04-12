from nltk.tokenize import sent_tokenize
import numpy as np
import heapq
from preprocessing import preprocess_text
from representation import get_tfidf_matrix

def extractive_summary(text, num_sentences=3):
    sentences = sent_tokenize(text)
    processed = [preprocess_text(s) for s in sentences]
    tfidf_matrix, _ = get_tfidf_matrix(processed)
    sentence_scores = np.sum(tfidf_matrix, axis=1)
    top_indices = heapq.nlargest(num_sentences, range(len(sentence_scores)), key=sentence_scores.__getitem__)
    top_indices.sort()
    return ' '.join([sentences[i] for i in top_indices])