# First Solution
def First_Solution(number):
    print("Iteration for First Solution is only 1 time process")
    return number*(number+1)//2

x = 5
result = First_Solution(x)
print(f"The sum of the first {x} number using the first solution is = {result}")
print()

# Second Solution
def Second_Solution(number):
    sum = 0
    iteration = 0
    for i in range(1, number+1):
        iteration = iteration+1
        sum = sum+i

    print(f"Iteration for second solution if {iteration} time proccess")
    return sum

x = 5
result = Second_Solution(x)
print(f"The sum of the first {x} number using the second solution is = {result}")
print()

#  Third Solution
def Third_Solution(number):
    sum = 0
    iteration = 0

    for i in range(1, number+1):
        for j in range(1, i+1):
            sum = sum+1
            iteration = iteration+1
    
    print(f"Iteration for third solution if {iteration} time proccess")
    return sum

x = 5
result = Third_Solution(x)
print(f"The sum of the first {x} number using the third solution is = {result}")
print()