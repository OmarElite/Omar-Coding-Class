def SwapMethod1(a, b):
    # Using XOR
    a = a ^ b
    b = a ^ b
    a = a ^ b

    print("After Swaping with first method : ")
    print(f"a = {a}")
    print(f"b = {b}")
    print()

def SwapMethod2(a, b):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1

    print("After Swapping with Second Method : ")
    print(f"a = {a}")
    print(f"b = {b}")
    print()

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

print("Original Number : ")
print(f"a = {a}")
print(f"b = {b}")
print()

SwapMethod1(a, b)
SwapMethod2(a, b)
