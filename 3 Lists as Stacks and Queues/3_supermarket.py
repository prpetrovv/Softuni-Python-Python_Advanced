from collections import deque

command = input()
people_left = deque([])
while command != "End":
    if command == "Paid":
        while people_left:
            print(people_left.popleft())
    else:
        people_left.append(command)
    command = input()

print(f"{len(people_left)} people remaining.")
