import pandas as pd
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv("data/spotify_millsongdata.csv")
df = df[['song', 'artist', 'text']].dropna()

# Reduce size for safety
df = df.sample(12000, random_state=42).reset_index(drop=True)

# Clean lyrics
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text

df['clean_text'] = df['text'].apply(clean_text)

# TF-IDF
tfidf = TfidfVectorizer(stop_words='english', max_features=6000)
tfidf_matrix = tfidf.fit_transform(df['clean_text'])

# Save objects
pickle.dump(df, open("songs.pkl", "wb"))
pickle.dump(tfidf, open("tfidf.pkl", "wb"))
pickle.dump(tfidf_matrix, open("tfidf_matrix.pkl", "wb"))

print("TF-IDF model prepared successfully!")
