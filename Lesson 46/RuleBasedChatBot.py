import re
import random
from colorama import Fore, init

# Initialise colorama
init(autoreset=True)

# Data structures for travel recommendations and jokes
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["New York", "Casablanca", "Paris"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# Function to greet the user
def GreetUser():
    print(f"{Fore.CYAN} Hello, I am Travel bot, your virtual Travel assistant")
    name = input(f"{Fore.YELLOW} What is your Name ?  ")
    print(f"{Fore.GREEN} Nice to meet you {name}, how can I assist you today ?  ")
    return name

# Function to show help options
def ShowHelp():
    print(f"{Fore.MAGENTA} I can assist you with the following : ")
    print(f"{Fore.GREEN} - Provide Travel Recommandation")
    print(f"{Fore.GREEN} - Offer packing Tips")
    print(f"{Fore.GREEN} - Tell Travel Jokes")
    print(f"{Fore.CYAN} Just ask me a question or type 'exit' to leave")

# Function to process user input
def process_user_input(user_input):
    # Convert Input to lower case and remove extra spaces
    user_input = user_input.strip().lower()
    user_input = re.sub(r'\s+', ' ', user_input)
    return user_input

# Function to provide travel recommendations
def ProvideTravelRecommendations():
    print(f"{Fore.CYAN} Travel Bot : Are you intresed in beach, Mountains or Cities ? ")
    preference = input(f"{Fore.YELLOW} You : ")
    preference = process_user_input(preference)

    if preference in destinations:
        suggestions = random.choice(destinations[preference])
        print(f"{Fore.GREEN} Travel Bot : How about visiting {suggestions} ? ")
        print(f"{Fore.CYAN} Travel Bot : Do you like this suggetion ? ( yes / no )")
        response = input(f"{Fore.YELLOW} You : ").strip().lower()

# Function to check flight status (simulated)


# Function to offer packing tips


# Function to tell a joke


# Main chat function


# Start the chatbot

