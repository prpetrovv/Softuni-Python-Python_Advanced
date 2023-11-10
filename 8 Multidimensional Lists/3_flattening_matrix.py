matrix = []
lines = int(input())
for line in range(lines):
    matrix.append([int(x) for x in input().split(', ')])

flat = []
for row in matrix:
    for number in row:
        flat.append(number)

print(flat)
