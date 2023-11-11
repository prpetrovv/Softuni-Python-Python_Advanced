from collections import deque

rows, cols = map(int, input().split())
snake = deque(x for x in input())
new_string = snake
matrix = [['' for i in range(cols)] for j in range(rows)]
for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            if new_string:
                if matrix[row][col] == '':
                    removed = new_string.popleft()
                    matrix[row][col] = removed
                    new_string.append(removed)
    else:
        for col in range(cols - 1, -1, -1):
            if new_string:
                if matrix[row][col] == '':
                    removed = new_string.popleft()
                    matrix[row][col] = removed
                    new_string.append(removed)

for submatrix in matrix:
    print(''.join(submatrix))
