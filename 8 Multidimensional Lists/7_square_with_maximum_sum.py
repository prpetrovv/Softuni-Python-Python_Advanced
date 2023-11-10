import sys

rows, columns = [int(x) for x in input().split(', ')]
matrix = []
max_square = -sys.maxsize
for row in range(rows):
    matrix.append([int(number) for number in input().split(', ')])

for row in range(rows - 1):
    for column in range(0, columns - 1):
        current = matrix[row][column] + matrix[row][column + 1] + matrix[row + 1][column] + matrix[row + 1][column + 1]
        if current > max_square:
            first = f"{matrix[row][column]} {matrix[row][column + 1]}"
            second = f"{matrix[row + 1][column]} {matrix[row + 1][column + 1]}"
            max_square = current

print(first)
print(second)
print(max_square)
