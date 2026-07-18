# 📝 Text Summarization Console App

A powerful Python application that provides **extractive** and **abstractive** text summarization with automatic evaluation metrics. This project demonstrates natural language processing techniques using both classical TF-IDF methods and state-of-the-art transformer models.

## ✨ Features

- **Extractive Summarization**: Selects the most important sentences from the original text using TF-IDF scoring
- **Abstractive Summarization**: Generates new, concise summaries using the T5 transformer model
- **Text Preprocessing**: Automatic cleaning, tokenization, and stopword removal
- **Evaluation Metrics**: ROUGE score calculation (ROUGE-1, ROUGE-2, ROUGE-L) with precision, recall, and F1 scores
- **Web UI**: Interactive Streamlit interface for easy text input and summary generation
- **Flexible Input**: Upload text files or paste text directly

## 🛠️ Prerequisites

- Python 3.7+
- pip (Python package manager)

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/hiruthicksm-19/Text-Summarization.git
cd Text-Summarization/text_summarizer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### Required Packages
- **nltk**: Natural language processing toolkit for tokenization and stopword removal
- **transformers**: Hugging Face library for T5 model access
- **torch**: PyTorch for deep learning model inference
- **scikit-learn**: Machine learning utilities for TF-IDF vectorization
- **rouge-score**: ROUGE evaluation metric calculation
- **streamlit**: Web framework for the interactive UI

## 🚀 Quick Start

### Run the Streamlit Web App
```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

### Command Line Usage
```python
from extractive import extractive_summary
from abstractive import abstractive_summary
from evaluation import evaluate_summary

text = "Your text here..."

# Get extractive summary (top 3 sentences)
ext_summary = extractive_summary(text, num_sentences=3)

# Get abstractive summary (max 60 tokens)
abs_summary = abstractive_summary(text, max_len=60)

# Evaluate the abstractive summary
scores = evaluate_summary(text, abs_summary)
```

## 📁 Project Structure

```
text_summarizer/
├── app.py                 # Streamlit web interface
├── preprocessing.py       # Text cleaning and tokenization
├── representation.py      # TF-IDF vectorization
├── extractive.py         # Extractive summarization engine
├── abstractive.py        # Abstractive summarization (T5 model)
├── postprocessing.py     # Summary cleanup and formatting
├── evaluation.py         # ROUGE score evaluation
├── requirements.txt      # Project dependencies
├── input.txt            # Sample input text
├── summary.txt          # Sample output summary
└── README.md            # This file
```

## 🔍 How It Works

### Extractive Summarization Pipeline
1. **Input**: Original text
2. **Preprocessing**: Text cleaning, tokenization into sentences
3. **Vectorization**: Convert sentences to TF-IDF vectors
4. **Scoring**: Calculate importance scores for each sentence
5. **Selection**: Choose top N sentences by score
6. **Output**: Summary maintaining original sentence order

### Abstractive Summarization Pipeline
1. **Input**: Original text (up to 512 tokens)
2. **Tokenization**: Convert text to T5 token format
3. **Model Inference**: T5-small model generates new summary
4. **Decoding**: Beam search decoding for quality
5. **Output**: New concise summary text

### Evaluation
Uses ROUGE (Recall-Oriented Understudy for Gisting Evaluation) metrics:
- **ROUGE-1**: Unigram overlap between summary and reference
- **ROUGE-2**: Bigram (2-gram) overlap
- **ROUGE-L**: Longest common subsequence-based F1

Each metric returns precision, recall, and F1 score.

## ⚙️ Configuration & Parameters

### In the Streamlit UI:
- **Input Method**: Choose between uploading a file or pasting text
- **Extractive Summary - Number of Sentences**: 1-10 (default: 3)
- **Abstractive Summary - Max Length**: 20-150 tokens (default: 60)

### In Code:
```python
# Extractive
extractive_summary(text, num_sentences=3)

# Abstractive
abstractive_summary(text, max_len=60)
```

## 💡 Example Usage

### Web Interface
1. Open the app in your browser
2. Upload a `.txt` file or paste text in the text area
3. Adjust settings in the sidebar (optional)
4. Click "Summarize"
5. View results: extractive summary, abstractive summary, and ROUGE scores

### Python Script
```python
from extractive import extractive_summary
from abstractive import abstractive_summary
from postprocessing import clean_summary
from evaluation import evaluate_summary

text = """
Your long document here...
Multiple sentences describing a topic...
"""

# Generate both summaries
ext = clean_summary(extractive_summary(text, num_sentences=2))
abs = clean_summary(abstractive_summary(text, max_len=50))

print("Extractive:", ext)
print("Abstractive:", abs)

# Evaluate
scores = evaluate_summary(text, abs)
print("ROUGE Scores:", scores)
```

## 📊 Sample Output

**Original Text:**
> "Machine learning is a subset of artificial intelligence. It enables systems to learn and improve from experience without being explicitly programmed. Deep learning further extends this by using neural networks with multiple layers."

**Extractive Summary:**
> "Machine learning is a subset of artificial intelligence. Deep learning further extends this by using neural networks with multiple layers."

**Abstractive Summary:**
> "Machine learning uses AI systems to learn from experience. Deep learning extends this with multi-layer neural networks."

**ROUGE Scores:**
```json
{
  "rouge1": {"precision": 0.85, "recall": 0.72, "f1": 0.78},
  "rouge2": {"precision": 0.62, "recall": 0.51, "f1": 0.56},
  "rougeL": {"precision": 0.80, "recall": 0.67, "f1": 0.73}
}
```

## 🎯 Use Cases

- **News Articles**: Quickly summarize long articles
- **Research Papers**: Extract key findings
- **Meeting Notes**: Generate actionable summaries
- **Document Clustering**: Preprocess documents for similarity analysis
- **Content Moderation**: Summarize user-generated content for review

## ⚡ Performance Notes

- **T5-small model**: ~1-2 seconds per summarization (first run downloads model ~1GB)
- **TF-IDF extraction**: Instant for most text sizes
- **Memory**: ~2-3GB when T5 model is loaded
- **GPU Support**: Set up PyTorch with CUDA for faster inference

## 🐛 Troubleshooting

### NLTK Data Not Found
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### Model Download Issues
The T5 model will automatically download on first run. Ensure you have ~1GB free disk space.

### Memory Issues
For large texts (>10,000 words), consider:
- Splitting into smaller chunks
- Using `num_beams=2` instead of 4 in abstractive.py
- Running on a machine with more RAM

## 📈 Future Enhancements

- [ ] Support for multiple languages
- [ ] Fine-tuned domain-specific models
- [ ] Batch processing for multiple documents
- [ ] Export results as PDF/Word
- [ ] Comparison view between extractive and abstractive
- [ ] Custom model training interface

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Hiruthick SM**
- Email: hiruthickchemist@gmail.com
- LinkedIn: [linkedin.com/in/hiruthick](https://www.linkedin.com/in/hiruthick)
- GitHub: [github.com/hiruthicksm-19](https://github.com/hiruthicksm-19)

## 🙌 Acknowledgments

- **Hugging Face** for the transformers library and T5 model
- **NLTK** for NLP toolkit
- **Streamlit** for the web framework
- **ROUGE Metric** original paper by Chin-Yew Lin

## 📚 References

- [T5: Text-to-Text Transfer Transformer](https://arxiv.org/abs/1910.10683)
- [ROUGE: A Package for Automatic Evaluation of Summaries](https://aclanthology.org/W04-1013/)
- [TF-IDF Wikipedia](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

---

**Made with ❤️ for NLP enthusiasts**