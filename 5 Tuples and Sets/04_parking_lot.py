car_numbers = set()
lines = int(input())

for _ in range(lines):
    direction, number = input().split(", ")
    if direction == "IN":
        car_numbers.add(number)
    elif direction == "OUT":
        car_numbers.remove(number)

if car_numbers:
    for car in car_numbers:
        print(car)
else:
    print("Parking Lot is Empty")
