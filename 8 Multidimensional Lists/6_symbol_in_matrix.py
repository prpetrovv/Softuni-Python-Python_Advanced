lines = int(input())
matrix = []
for _ in range(lines):
    matrix.append(list(input()))
to_find = input()
found = False
for row_i in range(lines):
    for char_i in range(lines):
        if matrix[row_i][char_i] == to_find:
            print(f"({row_i}, {char_i})")
            found = True
            break
    if found:
        break
if not found:
    print(f"{to_find} does not occur in the matrix")
