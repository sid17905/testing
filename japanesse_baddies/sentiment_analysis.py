# Import libraries
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import re

# Download vader lexicon (only first time)
nltk.download('vader_lexicon')

# Initialize analyzer
sia = SentimentIntensityAnalyzer()

# -----------------------------
# Load dataset
# -----------------------------
data = pd.read_csv(r"C:\Users\dhanr\OneDrive\Desktop\ollama_projects\nltk\reviews.csv")

# -----------------------------
# Clean text function
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text

data["clean_review"] = data["review"].apply(clean_text)

# -----------------------------
# Sentiment analysis function
# -----------------------------
def analyze_sentiment(text):

    score = sia.polarity_scores(text)
    compound = score['compound']

    if compound >= 0.05:
        return "Positive"

    elif compound <= -0.05:
        return "Negative"

    else:
        return "Neutral"

# Apply sentiment analysis
data["sentiment"] = data["clean_review"].apply(analyze_sentiment)

# Get sentiment scores
data["scores"] = data["clean_review"].apply(lambda x: sia.polarity_scores(x))

# -----------------------------
# Print results
# -----------------------------
print("\nCustomer Reviews with Sentiment:\n")
print(data[["review", "sentiment"]])

# -----------------------------
# Sentiment summary
# -----------------------------
print("\nSentiment Count:\n")
print(data["sentiment"].value_counts())

# -----------------------------
# Visualization
# -----------------------------
data["sentiment"].value_counts().plot(kind="bar")

plt.title("Customer Review Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.show()