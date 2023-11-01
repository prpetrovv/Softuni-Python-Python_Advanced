from collections import deque

people = deque(input().split())
number = int(input())
count = 1
while len(people) > 1:
    removed = people.popleft()
    if count == number:
        print(f"Removed {removed}")
        count = 1
        continue
    people.append(removed)
    count += 1
print(f"Last is {people[0]}")
