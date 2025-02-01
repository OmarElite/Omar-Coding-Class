def ReverseString(word):
    if len(word) == 1:
        return word[0]
    
    first_character = word[0]
    reverse_word = ReverseString(word[1:]) + first_character
    return reverse_word

text = input("Enter any Sentence :  ")
result = ReverseString(text)
print(f"The Reverse String is : {result}")