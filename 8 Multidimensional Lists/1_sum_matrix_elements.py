numbers = input().split(', ')

matrix = []
rows = int(numbers[0])
n_numbers = int(numbers[1])

sum_numbers = 0

for i in range(rows):
    current = [int(k) for k in input().split(', ')]
    for k in current:
        sum_numbers += k
    matrix.append(current)

print(sum_numbers)
print(matrix)
