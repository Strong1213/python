# sentiment_dashboard.py

import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

st.title("📊 AI-Powered Feedback Sentiment Dashboard")

# Session state for storing feedback
if "feedback_list" not in st.session_state:
    st.session_state.feedback_list = []

# Input box
feedback = st.text_area("✍️ Enter your feedback:")

if st.button("Analyze"):
    if feedback.strip() != "":
        scores = analyzer.polarity_scores(feedback)
        if scores['compound'] >= 0.05:
            sentiment = "Positive"
        elif scores['compound'] <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        st.session_state.feedback_list.append({"Feedback": feedback, "Sentiment": sentiment})
        st.success(f"✅ Sentiment: {sentiment}")

# Show collected feedback
if st.session_state.feedback_list:
    df = pd.DataFrame(st.session_state.feedback_list)

    st.subheader("📋 All Feedback")
    st.dataframe(df)

    # Sentiment counts
    counts = df["Sentiment"].value_counts()

    st.subheader("📊 Sentiment Distribution")
    fig, ax = plt.subplots()
    counts.plot(kind="bar", ax=ax)
    plt.xticks(rotation=0)
    st.pyplot(fig)

    # Export option
    st.download_button("⬇️ Download Results (CSV)", df.to_csv(index=False), "feedback_results.csv")
