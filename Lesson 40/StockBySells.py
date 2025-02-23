def CalculateProfits(arr, arr_size):
    profit = 0
    for i in range(1, arr_size):
        # if the current elemnt is greater then the last elemnt than we will buy the previous day and sell the current day
        if arr[i] > arr[i-1]:
            profit = profit + arr[i] - arr[i-1]

    return profit

price = []

for i in range(7): # Getting stock prices for 7 days
    element = int(input(f"Enter stock price of day {i+1} : "))
    price.append(element)

print("Stock price for 7 days : ")
print(price)

result = CalculateProfits(price, len(price))
print(f"Maximum profit = {result}")
