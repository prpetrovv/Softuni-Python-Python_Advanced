class FahrenheitError(Exception):
    min_f = 32
    max_f = 212

    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f'The {self.f} is not a valid range {self.min_f, self.max_f}'


def fahrenheit_to_celsius(f: float) -> float:
    if f < FahrenheitError.min_f or f > FahrenheitError.max_f:
        raise FahrenheitError(f)
    return (f - 32) * 5 / 9


value = input('Enter a temperature in Fahrenheit: ')

try:
    f = float(value)

except ValueError as error:
    print(error)
else:
    try:
        result = fahrenheit_to_celsius(f)

    except FahrenheitError as error:
        print(error)
    else:
        print(f'{f} Fahrenheit = {result:.4f} Celsius')
