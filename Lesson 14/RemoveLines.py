# Remove lines Starti gwith any Prefixe

f1 = open("Sample1.txt", "r")
f2 = open("Sample3.txt", "w")

#Reading eich lines from original Sample1.txt
for content in f1.readlines():
    if not (content.startswith("Hello")): # Reading all lines that not started with word 'Hello'
        f2.write(content)

f1.close()
f2.close()
