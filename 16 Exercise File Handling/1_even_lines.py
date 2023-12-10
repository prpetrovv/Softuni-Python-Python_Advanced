symbols_to_replace = {"-", ",", ".", "!", "?"}
with open("text.txt", "r") as my_file:
    file_information = my_file.readlines()
for row in file_information:
    for symbol in symbols_to_replace:
        row = row.replace(symbol, "@")
    reversed_row = row.split()
    reversed_row.reverse()
    print(''.join(reversed_row))
