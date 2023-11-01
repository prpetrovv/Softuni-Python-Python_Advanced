def reverse_numbers(numbers_string):
    numbers_list = numbers_string.split(" ")
    reversed_list = list()
    while numbers_list:
        reversed_list.append(numbers_list.pop())
    print(" ".join(reversed_list))


reverse_numbers(input())
