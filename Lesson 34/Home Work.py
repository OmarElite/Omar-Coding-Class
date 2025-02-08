def is_power_of_two(n):
    return (n & (n - 1)) == 0 and n > 0

a = int(input("Enter 'a' for a*b: "))
b = int(input("Enter 'b' for a*b: "))

product = a * b
print(f"Product of {a} and {b} is: {product}")

if is_power_of_two(product):
    print(f"{product} is a power of 2.")
else:
    print(f"{product} is NOT a power of 2.")
    