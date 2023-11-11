rows, columns = map(int, input().split())
start = ord('a')
matrix = []
for row in range(rows):
    submatrix = []
    for col in range(columns):
        my_string = chr(start + row) + chr(start + row + col) + chr(start + row)
        submatrix.append(my_string)
    print(*submatrix)
