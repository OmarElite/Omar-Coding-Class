def OddOccurringNumber(Array1):
    result = 0

    for element in Array1:
        result = result ^ element
        
    return result

MyList = []
ListSize = int(input("Enter The List Size :  "))

while ListSize:
    number = int(input("Enter number for your list element :  "))
    MyList.append(number)
    ListSize = ListSize - 1

result = OddOccurringNumber(MyList)

print()
print(f"The Odd Occurring number is {result}")
