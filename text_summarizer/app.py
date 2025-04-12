import streamlit as st
from extractive import extractive_summary
from abstractive import abstractive_summary
from postprocessing import clean_summary
from evaluation import evaluate_summary

st.set_page_config(page_title="Text Summarizer", layout="wide")

def main():
    
    st.title("📝 Text Summarizer App")

    st.markdown("""
    This app provides both **Extractive** and **Abstractive** summarization.
    Upload or paste your text below, then click **Summarize**.
    """)

    # Input Section
    input_method = st.radio("Choose Input Method", ("Upload File", "Paste Text"))

    if input_method == "Upload File":
        uploaded_file = st.file_uploader("Choose a text file", type="txt")
        if uploaded_file is not None:
            text = uploaded_file.read().decode("utf-8")
        else:
            text = ""
    else:
        text = st.text_area("Enter your text below", height=300)

    # Sidebar settings
    with st.sidebar:
        st.header("⚙️ Settings")
        num_sentences = st.slider("Extractive Summary - Number of Sentences", 1, 10, 3)
        max_length = st.slider("Abstractive Summary - Max Length", 20, 150, 60)

    # Generate Summaries
    if st.button("Summarize") and text.strip():
        with st.spinner("Generating Extractive Summary..."):
            ext_summary = extractive_summary(text, num_sentences=num_sentences)
            ext_summary = clean_summary(ext_summary)

        with st.spinner("Generating Abstractive Summary..."):
            abs_summary = abstractive_summary(text, max_len=max_length)
            abs_summary = clean_summary(abs_summary)

        with st.spinner("Evaluating Abstractive Summary..."):
            scores = evaluate_summary(text, abs_summary)

        # Output Results
        st.subheader("📌 Extractive Summary")
        st.write(ext_summary)

        st.subheader("📌 Abstractive Summary")
        st.write(abs_summary)

        st.subheader("📊 ROUGE Scores")
        st.json(scores)

    elif text.strip() == "":
        st.info("Please upload a file or paste some text to summarize.")


# 🔽 Custom Footer
footer = """
<style>
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    background-color: #f0f2f6;
    color: #262730;
    text-align: center;
    padding: 12px;
    font-size: 15px;
    border-top: 1px solid #e6e6e6;
}

.footer a {
    color: #1f77b4;
    text-decoration: none;
    margin: 0 10px;
}

.footer a:hover {
    text-decoration: underline;
}
</style>

<div class="footer">
    Developed by <strong>Hiruthick SM</strong> |
    <a href="mailto:hiruthickchemist@gmail.com" target="_blank">Email</a> |
    <a href="https://www.linkedin.com/in/hiruthick" target="_blank">LinkedIn</a> |
    <a href="https://github.com/hiruthicksm-19" target="_blank">GitHub</a>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
