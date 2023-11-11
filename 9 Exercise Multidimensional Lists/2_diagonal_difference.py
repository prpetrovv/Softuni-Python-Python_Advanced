rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

primary_diagonal = [matrix[i][i] for i in range(rows)]
secondary_diagonal = [matrix[i][rows - i - 1] for i in range(rows)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
