class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def add_numbers(self):
        result = self.num1 + self.num2 + self.num3
        print("The result of adding the three numbers is:", result)

expression1 = Expression(5, 10, 15)
expression1.add_numbers()
