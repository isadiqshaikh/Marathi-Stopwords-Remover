import streamlit as st

# Marathi stopwords list (you can expand this later)
stopwords = set([
    "आहे", "की", "मध्ये", "आणि", "वर", "होते", "त्याने", "ती", "तो", "हे", "सर्व", "मी",
    "आहेत", "आपण", "नाही", "त्याला", "त्याची", "त्यात", "का", "पण", "जसे", "ही", "आणखी", "किंवा"
])

# Function to tokenize text (simple split)
def tokenize_text(text):
    return text.split()

# Function to remove stopwords
def remove_marathi_stopwords(text):
    words = tokenize_text(text)
    filtered_words = [word for word in words if word not in stopwords]
    return " ".join(filtered_words)

# Streamlit UI
st.title("🧹 Marathi Stopwords Remover")

user_input = st.text_area("Enter Marathi text:")

if st.button("Clean Text"):
    if user_input.strip() != "":
        cleaned = remove_marathi_stopwords(user_input)
        st.markdown("### ✅ Cleaned Text:")
        st.success(cleaned)
    else:
        st.warning("Please enter some text.")

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
