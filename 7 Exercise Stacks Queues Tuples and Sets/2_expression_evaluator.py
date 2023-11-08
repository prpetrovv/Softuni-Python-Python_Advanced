import math
from functools import reduce

given = input().split(' ')
digits = []
for symbol in given:
    if symbol.lstrip('-').isdigit():
        digits.append(int(symbol))
    else:
        if symbol == "+":
            digits = [reduce(lambda x, y: x + y, digits)]
        elif symbol == "-":
            digits = [reduce(lambda x, y: x-y, digits)]
        elif symbol == "*":
            digits = [reduce(lambda x, y: x*y, digits)]
        elif symbol == "/":
            digits = [reduce(lambda x, y: x//y, digits)]
print(*digits)
