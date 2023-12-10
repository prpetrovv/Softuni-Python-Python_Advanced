symbols_to_replace = {"-", ",", ".", "!", "?"}
with open("text.txt", "r") as my_file:
    file_information = my_file.readlines()
for row in range(0, len(file_information), 2):
    for symbol in symbols_to_replace:
        file_information[row] = file_information[row].replace(symbol, "@")
    print(*file_information[row].split()[::-1], sep=" ")
