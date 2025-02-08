def BalancePrentheses(s, l, r, p, n):
    if p == 2 * n:
        for i in s:
            print(i, end="")
        print()

        return

    if l < n : # And an opening brackets if we have not reach the limit
        s[p] = "("
        BalancePrentheses(s, l+1, r, p+1, n)

    if r < l: # And a Closing Bracket if it will not make the string Invalid
        s[p] = ")"
        BalancePrentheses(s, l, r+1, p+1, n)
    
n = int(input("Enter the number of parentheses pears : "))
s = [""] * (2 * n)
print()

BalancePrentheses(s, 0, 0, 0, n)
