import nltk
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download("punkt")
nltk.download("stopwords")

def clean_text(text):
    text = re.sub(r"<.*?>", "", text)  # Remove HTML
    text = re.sub(r"\d+", "", text)  # Remove digits
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.lower()
    return text

def preprocess_text(text):
    clean = clean_text(text)
    words = word_tokenize(clean)
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words)