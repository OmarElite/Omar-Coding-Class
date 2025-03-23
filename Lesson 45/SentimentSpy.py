# Import necessary libraries
from textblob import TextBlob # - TextBlob for natural language processing tasks like sentiment analysis
import colorama # - Colorama for colored terminal output
from colorama import Fore, Style
import sys # - sys and time for animations and delays
import time

# Initialize Colorama to reset terminal colors automatically after each output
colorama.init(autoreset=True)

# Define global variables
username="" # - `user_name`: To store the name of the user (Agent)
ConversationHistory = [] # - `conversation_history`: A list to store all user inputs
positive_count = negative_count = neutral_count = 0 # - Sentiment counters (`positive_count`, `negative_count`, `neutral_count`) to track sentiment trends

# Define a function to simulate a processing animation
def ShowProcessingAnimation():
    print(f"{Fore.CYAN}🕵️ detecting Sentiment clues", end="") 
    # - Prints "loading dots" to make the chatbot feel interactive
    # - Use a loop to display three dots with a slight delay
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush() # Force the terminal to display the output imediately

# Define a function to analyze sentiment of the text
def AnalyseSentiment(text):
    global positive_count, negative_count, neutral_count

    try:
        # - Use TextBlob to calculate the polarity of the input text
        blob = TextBlob(text)

        # - Categorize the sentiment into "Very Positive," "Positive," "Neutral," "Negative," or "Very Negative"
        Sentiment = blob.sentiment.polarity

        # - Append the user input to `conversation_history`
        ConversationHistory.append(text)
        
        # - Update the sentiment counters based on the category
        if Sentiment > 0.75: # Very Positive
            positive_count = positive_count + 1
            return f"\n{Fore.GREEN} 🌟 Very Positive Sentiment detected, agent {username} ! (Score = {Sentiment:.2f})"
        elif 0.25 < Sentiment <= 0.75: # Positive
            positive_count = positive_count + 1
            return f"\n{Fore.GREEN} 🌟 Positive Sentiment detected, agent {username} ! (Score = {Sentiment:.2f})"
        elif -0.25 <= Sentiment <= 0.25:
            neutral_count = neutral_count + 1
            return f"\n{Fore.YELLOW} 😐 Neutral Sentiment detected, agent {username} ! (Score = {Sentiment:.2f})"
        elif -0.75 <= Sentiment < -0.25:
            negative_count = negative_count + 1
            return f"\n{Fore.RED} 💔 Negative sentiment detected, agent {username} ! (Score = {Sentiment:.2f})"
        else:
            negative_count = negative_count + 1
            return f"\n{Fore.RED} 💔 Very Negative sentiment detected, agent {username} ! (Score = {Sentiment:.2f})"
    except Exception as e:
        # - Handle exceptions to avoid crashes
        return f"\n{Fore.RED} An ERROR occured during Sentiment Analysing = {str(e)}"

# Define a function to handle commands
def ExecutCommand(command):
    # - Handle commands like `summary`, `reset`, `history`, and `help`
    # - `summary`: Displays the count of positive, negative, and neutral sentiments
    # - `reset`: Clears the conversation history and resets counters
    # - `history`: Shows all previous user inputs
    # - `help`: Displays a list of available commands
    # - Return appropriate responses for each command
    global ConversationHistory, positive_count, negative_count, neutral_count

    if command == "summary":
        return (f"{Fore.CYAN} 🕵️ Mission Report:\n"
                f"{Fore.GREEN} Positive Message Detected  = {positive_count}\n"
                f"{Fore.RED} Negative Message Detected = {negative_count}\n"
                f"{Fore.YELLOW} Neutral Message Detected = {neutral_count}")
    elif command == "reset":
        # Clear all datas
        ConversationHistory.clear()
        positive_count = negative_count = neutral_count = 0 # Reset all counters back to 0
        return (f"{Fore.CYAN} 🕵️ Mission Reset ... All previous Datas has been cleared")
    elif command == "history":
        return "\n".join([f"{Fore.CYAN}Message {i+1}: {msg}" for i, msg in enumerate(ConversationHistory)]) \
                if ConversationHistory else f"{Fore.YELLOW} No conversation history available."
    elif command == "help":
        return (f"{Fore.CYAN} 🔍 Available commands:\n"
                f"- Type any sentence to analyse sentiment \n"
                f"- Type 'summary' to get a mission report or analyse sentiment \n"
                f"- Type 'reset' to clear all mission data and Start again \n"
                f"- Type 'history' to view all previous messages and analysis \n"
                f"- Type 'exit' to conclud your mission and leave the chat")
    else:
        return f"{Fore.RED} unknown command type 'help' for list of command"

# Define a function to validate the user's name
def GetValidName():
    # - Continuously prompt the user for a name until they enter a valid alphabetic string
    while True:
        name = input("What is Your Name ?  ").strip() # - Strip any extra spaces and ensure the input is not empty or invalid
        if name and name.isalpha(): # Make sure that the name is not empty and only containes letters or Alphabets
            return name
        else:
            print(f"{Fore.RED} Please enter a Valide Name with only Letters or Alphabets")

# Define the main function to start the chatbot
def StartSentimentChat():
    # - Display a welcome message and introduce the Sentiment Spy activity
    print(f"{Fore.CYAN}{Style.BRIGHT} 🕵️ Welcome to Sentiment Spy ! Your personal Emotion detective is here 🎉")

    # - Ask the user for their name and store it in the `user_name` variable
    global username 
    username = GetValidName()
    print(f"\n{Fore.CYAN} Nice to meet you Agent {username} ! Type your sentence to Analyse Emotion. Type 'help' for options ...")

    # - Enter an infinite loop to interact with the user:
    while True :
        #   - Prompt the user to enter a sentence or command
        user_input = input(f"\n{Fore.MAGENTA}{Style.BRIGHT} Agent {username} : {Style.RESET_ALL}").strip()
        
        #   - Check for empty input and prompt the user to enter a valid sentence
        #   - If the input matches specific commands (`exit`, `summary`, `reset`, `history`, `help`), execute the corresponding functionality
        #   - Otherwise, call the `analyze_sentiment` function to analyze the input text
        #   - Display the sentiment analysis result with color-coded feedback
        # - Exit the loop and display a final summary when the user types `exit`

# Define the entry point for the script
# - Ensure the chatbot starts only when the script is run directly (not imported)
# - Call the `start_sentiment_chat` function to begin the activity
