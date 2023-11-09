from collections import deque


def check_and_add_crafted(toy_type):
    if toy_type in crafted_toys.keys():
        crafted_toys[toy_type] += 1
    else:
        crafted_toys[toy_type] = 1


materials_list = deque(int(x) for x in input().split())
magic_list = deque(int(x) for x in input().split())
crafted_toys = {}

while magic_list and materials_list:
    curr_material = materials_list.pop()
    if curr_material == 0:
        continue
    curr_magic = magic_list.popleft()
    if curr_magic == 0:
        materials_list.append(curr_material)
        continue
    result = curr_magic * curr_material
    if result < 0:
        result = curr_material + curr_magic
        materials_list.append(result)
    elif result == 150:
        check_and_add_crafted("Doll")
    elif result == 250:
        check_and_add_crafted("Wooden train")
    elif result == 300:
        check_and_add_crafted("Teddy bear")
    elif result == 400:
        check_and_add_crafted("Bicycle")
    else:
        materials_list.append(curr_material + 15)

if ("Doll" in crafted_toys.keys() and "Wooden train" in crafted_toys.keys()) or (
        "Teddy bear" in crafted_toys.keys() and "Bicycle" in crafted_toys.keys()):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials_list:
    materials_list.reverse()
    materials_string = ", ".join([str(x) for x in materials_list])
    print(f"Materials left: {materials_string}")

if magic_list:
    magic_string = ", ".join([str(x) for x in magic_list])
    print(f"Magic left: {magic_string}")
[print(f"{key}: {value}") for key, value in sorted(crafted_toys.items())]
