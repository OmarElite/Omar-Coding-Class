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
        if Sentiment > 0.75:
            positive_count = positive_count + 1
            return f"\n{Fore.GREEN}🌟 very Positive Sentiment detected, agent {username}! (score = {Sentiment:.2f})"
        elif -0.25 <= Sentiment <= 0.25:
            neutral_count = neutral_count + 1
            return f"\n{Fore.YELLOW}😐 Neutral Sentiment detected, agent {username}! (score = {Sentiment:.2f})"
        elif -0.75 <= Sentiment < -0.25:
            negative_count = negative_count + 1
            return f"\n{Fore.RED}💔 Negative sentiment detected, agent {username}! (score = {Sentiment:.2f})"
        else:
            negative_count = negative_count + 1
            return f"\n{Fore.RED}💔 Very Negative sentiment detected, agent {username}! (score = {Sentiment:.2f})"
    except Exception as e:
        # - Handle exceptions to avoid crashes
        return f"\n{Fore.RED} An ERROR occured during Sentiment Analysing = {str(e)}"

# Define a function to handle commands
# - Handle commands like `summary`, `reset`, `history`, and `help`
# - `summary`: Displays the count of positive, negative, and neutral sentiments
# - `reset`: Clears the conversation history and resets counters
# - `history`: Shows all previous user inputs
# - `help`: Displays a list of available commands
# - Return appropriate responses for each command

# Define a function to validate the user's name
# - Continuously prompt the user for a name until they enter a valid alphabetic string
# - Strip any extra spaces and ensure the input is not empty or invalid

# Define the main function to start the chatbot
# - Display a welcome message and introduce the Sentiment Spy activity
# - Ask the user for their name and store it in the `user_name` variable
# - Enter an infinite loop to interact with the user:
#   - Prompt the user to enter a sentence or command
#   - Check for empty input and prompt the user to enter a valid sentence
#   - If the input matches specific commands (`exit`, `summary`, `reset`, `history`, `help`), execute the corresponding functionality
#   - Otherwise, call the `analyze_sentiment` function to analyze the input text
#   - Display the sentiment analysis result with color-coded feedback
# - Exit the loop and display a final summary when the user types `exit`

# Define the entry point for the script
# - Ensure the chatbot starts only when the script is run directly (not imported)
# - Call the `start_sentiment_chat` function to begin the activity
