def TwoOddOccurringNumber(Array, ArraySize):
    XORof2 = Array[0]
    X = 0
    Y = 0
    SetBit = 0

    for i in range(1, ArraySize):
        XORof2 = XORof2 ^ Array[i]
    
    SetBit = XORof2 & ~(XORof2 - 1)

    for i in range(ArraySize):
        if Array[i] & SetBit:
            X = X ^ Array[i]
        else:
            Y = Y ^ Array[i]

    print(f"Two Odd Occurring numbers are :  {X} and {Y}")

MyList = []
Array_Size = int(input("Enter the size of the List :  "))

for i in range(Array_Size):
    num = int(input("Enter the number element of the list :  "))
    MyList.append(num)

TwoOddOccurringNumber(MyList, Array_Size)
