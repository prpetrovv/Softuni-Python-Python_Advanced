def reversed_string(given_string):
    my_list = list(given_string)
    reversed_string = ''
    while my_list:
        reversed_string += my_list.pop()
    return reversed_string


print(reversed_string(input()))
