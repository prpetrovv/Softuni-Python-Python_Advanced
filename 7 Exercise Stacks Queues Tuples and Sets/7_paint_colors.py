from collections import deque

primal_list = deque(input().split())
main_colors = ["blue", "red", "yellow"]
secondary_colors = ["purple", "orange", "green"]
found_colors = []
all_colors = main_colors + secondary_colors
while len(primal_list) > 1:
    first = primal_list.popleft()
    second = primal_list.pop()
    result_1 = first + second
    if result_1 in all_colors:
        found_colors.append(result_1)
    elif second + first in all_colors:
        found_colors.append(second + first)
    else:
        first = first[0:-1]
        if first:
            primal_list.insert(len(primal_list) // 2, first)
        second = second[0:-1]
        if second:
            primal_list.insert(len(primal_list) // 2, second)
else:
    if primal_list:
        if primal_list[0] in all_colors:
            found_colors.append(primal_list.pop())

for color in found_colors:
    if color == "orange":
        if ("red" not in found_colors) or ("yellow" not in found_colors):
            found_colors.remove("orange")
    elif color == "purple":
        if ("red" not in found_colors) or ("blue" not in found_colors):
            found_colors.remove("purple")
    elif color == "green":
        if ("blue" not in found_colors) or ("yellow" not in found_colors):
            found_colors.remove("green")

print(found_colors)
