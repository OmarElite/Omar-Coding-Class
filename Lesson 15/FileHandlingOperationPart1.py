
with open("Sample4.txt", "w") as file:
    file.write("Hello, I am Omar")

file.close()

# Split file into words
with open("Sample1.txt", "r") as file:
    data = file.readlines()

    print("Word in this file are = ")

    for line in data:
        word = line.split()
        print(word)

    print()

file.close()