from functools import reduce


def operate(sign, *args):
    return reduce(lambda a, b: eval(f"{a}{sign}{b}"), args)

    # def add():
    #     return sum(args)
    #
    # def subtract():
    #     result = functools.reduce(lambda a, b: a - b, args)
    #     return result
    #
    # def multiply():
    #     return functools.reduce(lambda a, b: a * b, args)
    #
    # def divide():
    #     return functools.reduce(lambda a, b: a / b, args)
    #
    # if sign == '+':
    #     return add()
    # elif sign == '-':
    #     return subtract()
    # elif sign == '/':
    #     return divide()
    # elif sign == '*':
    #     return multiply()


print(operate("-", 15, 3))
