def sum_numbers(file_name):
    data = open(file_name, 'r')
    sum_n = 0
    for number in data:
        sum_n += int(number)
    return sum_n


print(sum_numbers('numbers.txt'))
