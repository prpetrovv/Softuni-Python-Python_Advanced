f_matrix = []

lines = int(input())
for line in range(lines):
    info = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    f_matrix.append(info)
print(f_matrix)
