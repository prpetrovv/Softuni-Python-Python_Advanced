racks = 1
clothes = [int(x) for x in input().split()]
capacity = int(input())
current = 0

while clothes:
    item = clothes.pop()
    if current + item > capacity:
        racks += 1
        current = item
    elif current + item == capacity:
        current = 0
        if clothes:
            racks += 1
    else:
        current += item
print(racks)
