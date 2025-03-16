print("Hello I am your AI robot, What's your name ?")
name = input("You :  ")
print(f"Nice to meet you {name}")
print()

print("How is your feeling today ?  ")
feeling = input("You :  ")
feeling = feeling.lower() # To convert the answer into lowercase

if "good" in feeling or "great" in feeling or "happy" in feeling:
    print("I am glad to hear that !")
elif "bad" in feeling or "sad" in feeling or "angry" in feeling:
    print("I am sorry to hear that, I hope things will get better for you")
else:
    print("I see. Sometimes it's hard to put feelings into words")
print()

print("How old are you ?")
age = int(input("You :  "))
if age >= 18:
    print("You are eligible to get your Drive license")
elif age < 18:
    print("You are not eligible to get your Drive license")
print()
