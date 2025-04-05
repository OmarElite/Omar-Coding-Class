import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

choices = ["rock", "paper", "scissors"]
ai_memory = []

def ai_move():
    # Simple AI strategy: favor the move that beats the player's last move
    if not ai_memory:
        return random.choice(choices)

    last_player_move = ai_memory[-1]
    counter_moves = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }
    return counter_moves[last_player_move]

def determine_winner(player, ai):
    if player == ai:
        return Fore.YELLOW + "It's a tie!"
    elif (player == "rock" and ai == "scissors") or \
         (player == "paper" and ai == "rock") or \
         (player == "scissors" and ai == "paper"):
        return Fore.GREEN + "You win!"
    else:
        return Fore.RED + "AI wins!"

def main():
    print(Fore.CYAN + Style.BRIGHT + "Welcome to Rock-Paper-Scissors with AI!\n")
    while True:
        player_choice = input(Fore.CYAN + "Choose rock, paper, or scissors (or 'quit' to stop): ").lower()

        if player_choice == 'quit':
            print(Fore.MAGENTA + "Thanks for playing! See you next time.")
            break

        if player_choice not in choices:
            print(Fore.RED + "Invalid choice. Try again.")
            continue

        ai_choice = ai_move()
        print(Fore.BLUE + f"AI chose: {ai_choice}")

        result = determine_winner(player_choice, ai_choice)
        print(result + "\n")

        ai_memory.append(player_choice)

if __name__ == "__main__":
    main()
