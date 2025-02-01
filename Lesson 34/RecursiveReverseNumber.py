def ReverseNumber(number):
    if number > 0:
        last_number = number % 10
        
        if number // 10 > 0:
            current_number = ReverseNumber((int(number // 10)))
            reverse = last_number * pow(10, len(str(current_number))) + current_number
            return reverse
        
        return number

num = int(input("Enter your number :  "))
result = ReverseNumber(num)
print(f"The Reverse number is {result}")
