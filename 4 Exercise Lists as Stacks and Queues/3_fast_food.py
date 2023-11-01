from collections import deque

available = int(input())
orders = deque(int(x) for x in input().split(" "))

biggest_order = max(orders)
print(biggest_order)
while orders:
    current = orders.popleft()
    if current > available:
        orders.appendleft(current)
        break
    else:
        available -= current
if orders:
    print(f"Orders left: {' '.join(str(x) for x in orders)}")
else:
    print("Orders complete")
