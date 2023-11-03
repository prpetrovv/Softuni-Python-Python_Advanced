number = int(input())
all_elements = set()
for _ in range(number):
    compounds = input().split()
    for com in compounds:
        all_elements.add(com)

for element in all_elements:
    print(element)
