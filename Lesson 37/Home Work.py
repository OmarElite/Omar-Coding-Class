def find_paths(n, m, path=""):
    if n == 1 and m == 1:
        print(path)
        return
    if n > 1:
        find_paths(n - 1, m, path + "d")  # Move down
    if m > 1:
        find_paths(n, m - 1, path + "r")  # Move right

# Get user input
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

# Find and print all possible paths
find_paths(n, m)
