# First Solution
def First_Solution(number):
    return number*(number+1)//2

x = 5
result = First_Solution(x)
print(f"The sum of the first {x} number using the first solution is = {result}")
print()

# Second Solution
def Second_Solution(number):
    sum = 0
    for i in range(1, number+1):
        sum = sum+i

    return sum

x = 5
result = Second_Solution(x)
print(f"The sum of the first {x} number using the second solution is = {result}")
print()

# Third Solution
def Third_Solution(number):
    sum = 0
    for i in range(1, number+1):
        for j in range(1, i+1):
            sum = sum+1
        
    return sum

x = 5
result = Third_Solution(x)
print(f"The sum of the first {x} number using the third solution is = {result}")
print()