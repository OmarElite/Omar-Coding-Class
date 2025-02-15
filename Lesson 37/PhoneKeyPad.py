KeyPad= ["", "", "abc", "def" , "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def DisplayCombination(combination, current, output, n):
    if current == n:
        print(*output, sep=",")
        return
    
    # Display all the posible combinations by iterating first 1 to 3 for number and finding index in depend
    for i in range(len(KeyPad[combination[current]])):
        output.append(KeyPad[combination[current]][i])
        DisplayCombination(combination, current+1, output, n)
        output.pop()

        if combination[current] == 0 or combination[current] == 1:
            return
    
combination = [4, 3, 4]
n = len(combination)
DisplayCombination(combination, 0, [], n)
