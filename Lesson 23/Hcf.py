
small_number = int(input("Enter the Small number :  "))
large_number = int(input("Enter the Large number :  "))

while small_number > 0:
    number_store = small_number
    small_number = large_number % small_number
    large_number = number_store

print(f"The Highest common factor is {large_number}")
 