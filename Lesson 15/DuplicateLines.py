# Reading input files
input_file = open("Sample6.txt", "r")

# Creating output files
output_file = open("Sample7.txt", "w")

# unique lines that already been read
line_read_so_far = set()

print("Eliminating duplicate lines")

for sentence in input_file:
    if sentence not in line_read_so_far: # check if the sentence in one line is unique
        output_file.write(sentence)
        line_read_so_far.add(sentence) # Add unique sentences to the line read so far

input_file.close()
output_file.close()
