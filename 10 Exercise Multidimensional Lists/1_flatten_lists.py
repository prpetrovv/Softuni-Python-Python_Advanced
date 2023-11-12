matrix = [[x for x in row.split()] for row in input().split("|")]

string_to_print = ""
for index in range(len(matrix) - 1, -1, -1):
    for el in matrix[index]:
        string_to_print += el + " "
print(string_to_print)
