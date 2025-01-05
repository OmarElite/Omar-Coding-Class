def CheckIfSameNumber(first_number, second_number):
    if first_number ^ second_number == 0:
        print("Both numbers are the same")
    else:
        print("Both numbers are not the same")

f_num = int(input("Enter the first number :  "))
s_num = int(input("Enter the second number :  "))

CheckIfSameNumber(f_num, s_num)
