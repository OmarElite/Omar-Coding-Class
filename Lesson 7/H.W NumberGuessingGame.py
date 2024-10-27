import random

# Generate a random original number between 1 and 100
original_number = random.randint(1, 100)

# Initialize guessed number
guessed_number = None

# Keep asking until the guess is correct
while guessed_number != original_number:
    guessed_number = int(input("Enter your guessed number (between 1 and 100): "))
    
    if guessed_number > original_number:
        print("Your guess is too high ! Try a lower number.")
        print()
    elif guessed_number < original_number:
        print("Your guess is too low ! Try a higher number.")
        print()
    else:
        print()
        print("Congratulations ! You guessed the correct number !")
        print()
        print()
