def RomanToInt(a):
    # Dictionary of Roman Unit to integer equivalent values
    Roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    result = 0

    for i in range(len(a)):
        if i + 1 < len(a) and (Roman[a[i]] < Roman[a[i+1]]):
            result = result-Roman[a[i]]
        else:
            result = result+Roman[a[i]]

    return result

RomanNumeral = input("Enter a Roman Numeral :  ")

print(f"Integer form of {RomanNumeral} is = {RomanToInt(RomanNumeral)}")
