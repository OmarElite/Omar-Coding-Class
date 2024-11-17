# Reading the first line of Sample1.txt
f = open("Sample1.txt", "r")

print("Reading the first line of Sample1.txt :")
print(f.readline())
print()

# Relocating the Cursor of the File at the Begining
f.seek(0)

# Reading the first Three lines of Sample1.txt
print("Reading the first Three lines of Sample1.txt :")
print(f.readline())
print(f.readline())
print(f.readline())
print()

f.seek(0)

# Reading all lines using loops
print("Reading all lines using loops")

for i in f:
    print(i)

f.close()
