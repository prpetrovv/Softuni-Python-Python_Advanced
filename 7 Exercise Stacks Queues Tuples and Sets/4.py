from collections import deque

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

honey_made = 0

while bees and nectar:
    if bees[0] <= nectar[-1]:
        symbol = symbols.popleft()
        bee, col_nectar = bees.popleft(), nectar.pop()
        if symbol == '+':
            honey_made += abs(bee + col_nectar)
        elif symbol == '-':
            honey_made += abs(bee - col_nectar)
        elif symbol == '/':
            if bee == 0 or col_nectar == 0:
                continue
            honey_made += abs(bee / col_nectar)
        elif symbol == '*':
            honey_made += abs(bee * col_nectar)
    else:
        nectar.pop()
print(f"Total honey made: {honey_made}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
