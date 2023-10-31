from collections import deque

water = int(input())
command = input()
people = deque()

while command != "Start":
    people.append(command)
    command = input()
command = input()
while command != "End":
    usage = command.split()
    if len(usage) > 1:
        water += int(usage[-1])
    else:
        liters_to_drink = int(command)
        if water >= liters_to_drink:
            water -= liters_to_drink
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")
    command = input()
print(f"{water} liters left")
