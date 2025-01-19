def circuit_logic(A, B, C):
    gate1 = A and B
    gate2 = not C
    gate3 = gate2 and B
    gate4 = gate1 or gate3
    return gate4

A = int(input("Enter value for A : "))
B = int(input("Enter value for B : "))
C = int(input("Enter value for C : "))

output = circuit_logic(A, B, C)
print("Output of the circuit (Q):", int(output))
