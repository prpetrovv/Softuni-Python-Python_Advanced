types_of_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
matrix = []
targets = 0
targets_hit = []
person = []
for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == 'A':
            person = [row, col]
        elif matrix[row][col] == 'x':
            targets += 1

n_commands = int(input())

for _ in range(n_commands):
    command = input().split()
    if len(command) == 2:
        direction = command.pop()
        cur_position = person.copy()
        while True:
            aimed_row = cur_position[0] + types_of_moves[direction][0]
            aimed_col = cur_position[1] + types_of_moves[direction][1]
            if 0 <= aimed_row <= 4 and 0 <= aimed_col <= 4:
                cur_position = [aimed_row, aimed_col]
                if matrix[cur_position[0]][cur_position[1]] == 'x':
                    matrix[cur_position[0]][cur_position[1]] = '.'
                    targets_hit.append(cur_position)
                    break
            else:
                break
    else:
        moves = int(command.pop())
        direction = command.pop()
        aimed_row = person[0] + types_of_moves[direction][0] * moves
        aimed_col = person[1] + types_of_moves[direction][1] * moves
        if not (0 <= aimed_row <= 4):
            if aimed_row < 0:
                aimed_row = 0
            else:
                aimed_row = 4
        if not (0 <= aimed_col <= 4):
            if aimed_col < 0:
                aimed_col = 0
            else:
                aimed_col = 4
        matrix[person[0]][person[1]], matrix[aimed_row][aimed_col] = matrix[aimed_row][aimed_col], \
            matrix[person[0]][person[1]]
        person = [aimed_row, aimed_col]
n_targets_hit = len(targets_hit)
if targets == n_targets_hit:
    print(f"Training completed! All {n_targets_hit} targets hit.")
else:
    print(f"Training not completed! {targets - n_targets_hit} targets left.")
for i in targets_hit:
    print(i)
