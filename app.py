import streamlit as st
import pickle
import re

# Load saved model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# URL detection function
def detect_urls(text):
    url_pattern = r'(https?://\S+|www\.\S+)'
    return re.findall(url_pattern, text)

# Keyword detection
def highlight_suspicious_words(text):
    suspicious_words = ["win", "prize", "money", "urgent", "click", "offer", "free"]
    return [word for word in suspicious_words if word in text.lower()]

# Streamlit UI
st.title("🔐 AI-Based Job & Scholarship Scam Detector")

user_input = st.text_area("Paste suspicious message here:")

if st.button("Analyze Message"):

    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Transform text
        test_vector = vectorizer.transform([user_input])
        prediction = model.predict(test_vector)
        probability = model.predict_proba(test_vector)

        scam_prob = round(probability[0][1] * 100, 2)

        # Display probability
        st.write(f"### Scam Probability: {scam_prob}%")

        # Risk level
        if scam_prob > 80:
            st.error("🚨 High Risk Scam")
        elif scam_prob > 50:
            st.warning("⚠ Moderate Risk")
        else:
            st.success("✅ Low Risk")

        # URL detection
        urls = detect_urls(user_input)
        if urls:
            st.write("### 🔗 Suspicious URLs Found:")
            st.write(urls)

        # Keyword detection
        suspicious = highlight_suspicious_words(user_input)
        if suspicious:
            st.write("### 🚩 Suspicious Keywords Detected:")
            st.write(suspicious)
