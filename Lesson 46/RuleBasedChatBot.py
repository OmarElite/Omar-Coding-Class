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
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about visiting {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like this suggestion? (yes/no)")
        response = input(Fore.YELLOW + "You: ").strip().lower()

        if response == "yes":
            print(f"{Fore.GREEN} TravelBot: Great! Have an amazing time in {suggestion}!")
        elif response == "no":
            print(f"{Fore.RED} TravelBot: No worries! Let's find another place.")
            ProvideTravelRecommendations()  # Recur to suggest another destination
        else:
            print(f"{Fore.RED} TravelBot: I didn't catch that. Let's start over.")
            ProvideTravelRecommendations()  # Recur to handle unexpected input

    else:
        print(f"{Fore.RED} TravelBot: Sorry, I don't have recommendations for that preference.")

    # Show the help options again
    ShowHelp()

# Function to check flight status (simulated)
# Function to offer packing tips
def offer_packing_tips():
    print(f"{Fore.CYAN} Travel Bot :  Where are you travelling to ?")
    destination = input(f"{Fore.YELLOW} You : ")
    destination = process_user_input(destination)

    print(f"{Fore.CYAN} TRavel Bot : How many days will you be staying ?")
    days = input(f"{Fore.YELLOW} You : ")
    print(f"{Fore.GREEN} Travel Bot : Packing tips for {days} days in {destination}")
    
    print("{Fore.GREEN)- Pack versatile clothing items.")
    print (f"{Fore.GREEN} Don't forget travel adapters and chargers.")
    print (f" {Fore. GREEN} Check the weather forecast before packing.")

# Function to tell a joke
def tell_joke():
    joke = random.choice (jokes)
    print(f"{Fore. YELLOW} TravelBot: {joke}")

# Main chat function
def chat():
    name = GreetUser()
    ShowHelp()
    while True:
        user_input = input(f"{Fore.YELLOW}{name}:")
        processed_input = process_user_input(user_input)
        if "recommendation" in processed_input or "suggest" in processed_input:
            ProvideTravelRecommendations()
        elif "pack" in processed_input or "packing" in processed_input:
            offer_packing_tips()
        elif "joke" in processed_input or "funny" in processed_input:
            tell_joke()
        elif "help" in processed_input:
            ShowHelp()
        elif "exit" in processed_input or "bye" in processed_input:
            print (Fore.CYAN + "TravelBot: Safe travels! Goodbye!") 
            break
        else:
            print (Fore.RED + "TravelBot: I'm sorry, I didn't quite catch that. Could you please rephrase?")

# Start the chatbot
if __name__ == "__main__":
    chat()
