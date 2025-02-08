def ClimbStairs(stairs):
    if stairs < 0:
        return 0

    # If no Stairs left we reach the top just return 1
    if stairs == 0:
        return 1
    
    one_step = 0
    two_steps = 0

    if stairs >= 2:
        two_steps = ClimbStairs(stairs-2)

    one_step = ClimbStairs(stairs-1)

    total_ways = one_step + two_steps
    return total_ways

steps = int(input("Enter number of Steps in your stair :  "))

result = ClimbStairs(steps)
print(f"Numbers of Combination to climb the stairs = {result}")
