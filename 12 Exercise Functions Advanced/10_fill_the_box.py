from collections import deque


def fill_the_box(*args):
    broken = False
    elements = deque(args)
    size = elements.popleft() * elements.popleft() * elements.popleft()
    while elements:
        current = elements.popleft()
        if current == "Finish":
            break
            # stop it
        if size >= current:
            size -= current
        else:
            rest_elements = [el for el in elements if el != "Finish"]
            el_sum = sum(rest_elements)
            difference = current - size
            return f"No more free space! You have {el_sum + difference} more cubes."
    if elements or size > 0:
        return f"There is free space in the box. You could put {size} more cubes."


print(fill_the_box(10, 10,

                   10, 40, "Finish", 2, 15,

                   30))
