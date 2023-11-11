rows, cols = map(int, input().split())
matrix = list(input().split() for _ in range(rows))

found = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        cur = matrix[row][col]
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row][col + 1] == matrix[row + 1][
            col + 1]:
            found += 1
print(found)
