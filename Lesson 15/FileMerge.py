# Reading Sample1.txt
with open("Sample1.txt") as f1:
    data1 = f1.read()

# Reading Sample3.txt
with open("Sample3.txt") as f2:
    data2 = f2.read()

# Merge two files with new lines as the gap
data1 = data1 + "\n\n"
data1 = data1 + data2

print("Merging two files :")

with open("Sample8.txt", "w") as f3:
    f3.write(data1)

f1.close()
f2.close()
f3.close()