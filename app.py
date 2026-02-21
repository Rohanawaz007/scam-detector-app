import streamlit as st
import pickle
import re

st.set_page_config(page_title="AI Scam Detector", page_icon="🔐", layout="centered")

# Custom Styling
st.markdown("""
<style>
.big-title {
    font-size:40px !important;
    font-weight:700;
}
.subtitle {
    font-size:18px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🔐 AI-Based Job & Scholarship Scam Detector</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Protecting students from fake job offers and scholarship fraud using AI & NLP.</p>', unsafe_allow_html=True)
st.divider()

if st.button("Analyze Message"):

    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        test_vector = vectorizer.transform([user_input])
        prediction = model.predict(test_vector)
        probability = model.predict_proba(test_vector)

        # 👉 CALCULATE scam_prob FIRST
        scam_prob = round(probability[0][1] * 100, 2)

        # Now display result
        st.write("### 📊 Scam Analysis Result")
        st.metric("Scam Probability", f"{scam_prob}%")

        if scam_prob > 80:
            st.error("🚨 High Risk Scam Detected")
        elif scam_prob > 50:
            st.warning("⚠ Moderate Risk – Be Careful")
        else:
            st.success("✅ Low Risk – Likely Safe")
            
            
st.divider()
st.markdown("""
---
Developed for Cybersecurity Hackathon  
AI Model: Logistic Regression + TF-IDF  
Accuracy: 95%
""")
