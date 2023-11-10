lines = int(input())
matrix = []
for column in range(lines):
    matrix.append([int(x) for x in input().split(' ')])

main_sum = 0
for i in range(lines):
    main_sum += matrix[i][i]
print(main_sum)
