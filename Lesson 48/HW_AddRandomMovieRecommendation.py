import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import Fore, Style

# Load dataset
df = pd.read_csv("imdb_top_1000.csv")

# Fill missing overviews
df['Overview'] = df['Overview'].fillna('')

# Welcome user
user_name = input("Welcome! Please enter your name: ")
print(f"\nHi {user_name} 👋! Choose an option:")
print("1. AI-based Recommendation")
print("2. Random Recommendation")

choice = input("Enter 1 or 2: ")

def sentiment_analysis(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def display_movie(movie):
    print(f"\n{Fore.CYAN}--- Movie Recommendation ---{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Title:{Style.RESET_ALL} {movie['Title']}")
    print(f"{Fore.YELLOW}Genre(s):{Style.RESET_ALL} {movie['Genre']}")
    print(f"{Fore.YELLOW}IMDB Rating:{Style.RESET_ALL} {movie['IMDB_Rating']}")
    print(f"{Fore.YELLOW}Overview:{Style.RESET_ALL} {movie['Overview']}")
    print(f"{Fore.YELLOW}Sentiment:{Style.RESET_ALL} {sentiment_analysis(movie['Overview'])}")

def ai_recommendation():
    genre = input("Enter preferred genre (e.g. Action, Drama, Comedy): ")
    mood = input("Describe your mood (e.g. happy, sad, excited): ")
    try:
        rating = float(input("Enter minimum IMDB rating (optional): ") or 0)
    except ValueError:
        rating = 0

    # Filter by genre and rating
    filtered = df[df['Genre'].str.contains(genre, case=False) & (df['IMDB_Rating'] >= rating)]

    if filtered.empty:
        print("No movies found with that criteria.")
        return

    # Use TF-IDF + cosine similarity for overview comparison
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(filtered['Overview'])
    mood_vec = tfidf.transform([mood])
    similarities = cosine_similarity(mood_vec, tfidf_matrix).flatten()
    top_idx = similarities.argmax()
    recommended_movie = filtered.iloc[top_idx]
    display_movie(recommended_movie)

def random_recommendation():
    random_movie = df.sample().iloc[0]
    display_movie(random_movie)

# Main logic
if choice == '1':
    ai_recommendation()
elif choice == '2':
    random_recommendation()
else:
    print("Invalid choice.")

# Repeat option
repeat = input("\nDo you want another recommendation? (yes/no): ").lower()
if repeat == 'yes':
    print("\nRestart the script to get another recommendation! 🎬")
else:
    print("Goodbye! 👋")
