import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time

# Initialize colorama
init(autoreset=True)

def load_data():
	try:
		df = pd.read_csv(r"C:\Users\Omar\Desktop\Omar\Omar Coding Class\Lesson 49\imdb_top_1000.csv")
		df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
		return df
	except FileNotFoundError:
		print(Fore.RED + f"Error: The file 'imdb_top_1000.csv' was not found.")
		exit()

movies_df = load_data()
