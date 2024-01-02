from collections import deque

worms = deque([int(x) for x in input().split()])
holes = deque([int(x) for x in input().split()])
start_worms = len(worms)

matches = 0
while worms and holes:
    cur_worm = worms.pop()
    if cur_worm <= 0:
        continue
    cur_hole = holes.popleft()
    if cur_hole == cur_worm:
        matches += 1
    else:
        worms.append(cur_worm - 3)

worms_left = "none" if not worms else ", ".join(map(str, worms))
holes_left = "none" if not holes else ", ".join(map(str, holes))

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if worms:
    print(f"Worms left: {', '.join([str(x) for x in worms])}")
else:
    if matches == start_worms:
        print("Every worm found a suitable hole!")
    else:
        print(f"Worms left: none")
print(f"Holes left: {', '.join([str(x) for x in holes])}" if holes else "Holes left: none")
