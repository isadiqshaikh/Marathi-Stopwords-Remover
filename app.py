import streamlit as st
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

# Sample large Marathi stopword list (you can expand it from external source)
marathi_stopwords = [
    "आहे", "होते", "नाही", "तर", "पण", "आणि", "हे", "या", "हा", "त्याने",
    "त्याची", "त्याला", "मी", "आपण", "आम्ही", "त्यांनी", "त्यांचा", "त्यांचे",
    "त्याच्या", "मध्ये", "वरील", "खाली", "सुद्धा", "एक", "असे", "होणार"
]

# Text Preprocessing
def preprocess_text(text):
    return text.lower()

# Tokenize text
def tokenize_text(text):
    return word_tokenize(text)

# Remove stopwords
def remove_stopwords(words, stopwords_list):
    return [word for word in words if word not in stopwords_list]

# Full processing pipeline
def remove_marathi_stopwords(text):
    text = preprocess_text(text)
    words = tokenize_text(text)
    filtered_words = remove_stopwords(words, marathi_stopwords)
    return " ".join(filtered_words)

# Streamlit Web App
st.title("Marathi Stopwords Remover")
st.write("This app removes common Marathi stopwords from your input text.")

# User input
user_input = st.text_area("Enter Marathi text here:")

if st.button("Clean Text"):
    if user_input.strip():
        cleaned = remove_marathi_stopwords(user_input)
        st.subheader("Cleaned Text:")
        st.success(cleaned)
    else:
        st.warning("Please enter some Marathi text.")

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
