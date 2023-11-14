def rectangle(length, width):
    if (isinstance(length, int)) and (isinstance(width, int)):
        def area(le, wid):
            return le * wid

        def perimeter(le, wid):
            return le * 2 + wid * 2

        return f"Rectangle area: {area(length, width)}\n" \
               f"Rectangle perimeter: {perimeter(length, width)}"
    else:
        return "Enter valid values!"


print(rectangle(2, 10))
