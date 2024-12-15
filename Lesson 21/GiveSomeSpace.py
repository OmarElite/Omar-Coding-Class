# Calculate Space Complexity
def Sum(number):
    return number*(number+1)/2

def ArraySum(array):
    sum = 0
    for element in array:
        sum = sum + element

    return sum

# finding sum of the first n number using recursive function
def SumN(number):
    result = 0
    if number <= 0:
        return
    else:
        result = number+SumN(number-1)
    return result

x = 5
print(f"The Sum of the first {x} number is = {Sum(x)}")
print()

MyList = [1, 6, 73, 763, 12, 56, 7]
print(f"The Sum of the elements in the Array is = {ArraySum(MyList)}")
print()

print(f"The Sum of the first {x} number using recursive function is = {SumN(x)}")
print()