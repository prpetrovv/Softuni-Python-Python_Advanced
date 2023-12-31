from string import punctuation

with open("text.txt", "r") as given_file:
    given_info = given_file.readlines()

output_file = open("output.txt", "w")
for i in range(len(given_info)):
    row = given_info[i]

    letters = 0
    marks = 0

    for symbol in row:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line{i+1} {''.join(row[:-1])} ({letters})({marks})\n")
output_file.close()
