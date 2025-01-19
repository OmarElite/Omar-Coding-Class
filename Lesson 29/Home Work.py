n = int(input("Enter your number: "))

max_ones = 0
cur_ones = 0

while n > 0:
    if n % 2 == 1:
        cur_ones += 1
        if cur_ones > max_ones:
            max_ones = cur_ones
    else:
        cur_ones = 0
    n //= 2

print("Longest consecutive 1's length:", max_ones)
