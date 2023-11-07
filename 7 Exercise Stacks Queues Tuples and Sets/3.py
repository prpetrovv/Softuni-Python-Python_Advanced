from collections import deque

chocolate = [int(x) for x in input().split(', ')]
milk = deque(map(int, (input().split(', '))))

milkshakes = 0


while milkshakes < 5 and chocolate and milk:
    flag = False
    if chocolate[-1] <=0:
        chocolate.pop()
        flag = True
    if milk[0] <= 0:
        milk.popleft()
        flag = True
    if flag:
        continue
    if chocolate[-1] == milk[0]:
        milkshakes += 1
        chocolate.pop()
        milk.popleft()
    else:
        cup_milk = milk.popleft()
        milk.append(cup_milk)
        chocolate[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join([str(x) for x in milk])}")
else:
    print("Milk: empty")