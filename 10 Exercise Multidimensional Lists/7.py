types_of_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
n_presents = int(input())
size = int(input())
matrix = []
nice_kids = 0
nice_kids_awarded = 0
all_awarded = 0
santa = []
out_of_presents = False
for row in range(size):
    matrix.append(input().split())
    for column in range(size):
        if matrix[row][column] == 'S':
            santa = [row, column]
        elif matrix[row][column] == 'V':
            nice_kids += 1

while True:
    command = input()

    if command == "Christmas morning" or nice_kids == nice_kids_awarded:
        break
    row_to_go = santa[0] + types_of_moves[command][0]
    col_to_go = santa[1] + types_of_moves[command][1]
    if 0 <= row_to_go < size:
        pass
    elif row_to_go < 0:
        row_to_go = 0
    elif row_to_go > size:
        row_to_go = size - 1
    if col_to_go < 0:
        col_to_go = 0
    elif col_to_go > size:
        col_to_go = size - 1
    if matrix[row_to_go][col_to_go] == 'V':
        if n_presents == all_awarded:
            out_of_presents = True
            break
        nice_kids_awarded += 1
        all_awarded += 1
        matrix[row_to_go][col_to_go] = 'X'
    elif matrix[row_to_go][col_to_go] == 'C':
        matrix[row_to_go][col_to_go] = 'S'
        matrix[santa[0]][santa[1]] = '-'
        for type_m, move in types_of_moves.items():
            cookie_awarded = matrix[santa[0] + move[0]][santa[1] + move[1]]
            if cookie_awarded == 'V':
                if all_awarded == n_presents:
                    out_of_presents = True
                    break
                nice_kids_awarded += 1
                all_awarded += 1
            elif cookie_awarded == 'X':
                if all_awarded == n_presents:
                    out_of_presents = True
                    break
                all_awarded += 1
            matrix[santa[0] + move[0]][santa[1] + move[1]] = '-'
    if out_of_presents:
        break
    matrix[row_to_go][col_to_go] = 'S'
    matrix[santa[0]][santa[1]] = '-'
    santa = [row_to_go, col_to_go]

for row in matrix:
    print(*row)
if nice_kids_awarded == nice_kids:
    print(f"Good job, Santa! {nice_kids_awarded} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_awarded} nice kid/s.")
