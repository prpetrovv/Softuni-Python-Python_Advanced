from collections import deque


def check_if_valid(length, r, c):
    return 0 <= r < length and 0 <= c < length


def add(r, c, value):
    matrix[r][c] += value


def subtract(r, c, value):
    matrix[r][c] -= value


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    change = deque(input().split())
    if change[0] == "END":
        break
    else:
        command = change.popleft()
        row, col, increment = [int(x) for x in change]
        if check_if_valid(n, row, col):
            if command == "Add":
                add(row, col, increment)
            elif command == "Subtract":
                subtract(row, col, increment)
        else:
            print("Invalid coordinates")

[print(*row) for row in matrix]
