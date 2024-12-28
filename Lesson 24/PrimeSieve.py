
def PrimeSieve(number):
    prime = [True for i in range(number+1)]
    currentNumber = 2

    while currentNumber*currentNumber <= number:
        if prime[currentNumber] == True:
            for i in range(currentNumber**2, number+1, currentNumber):
                prime[i] = False
        
        currentNumber = currentNumber+1

    prime[0] = False
    prime[1] = False

    for p in range(number+1):
        if prime[p]:
            print(p)


num = int(input("Enter number to find all of the prime numbers less then the number itself = "))
print()

print(f"Here is the PRIME number smaaler then or equal to {num}")

PrimeSieve(num)