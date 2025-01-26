def ArrayTotalSum(a):
    length = len(a)
    if length == 1:
        return a[0]
    
    # return current elemnt and received sum
    return a[0] + ArrayTotalSum(a[1:])

myList = [42, 75, 7, 9, 14]

result = ArrayTotalSum(myList)
print(f"Array total Sum = {result}")
