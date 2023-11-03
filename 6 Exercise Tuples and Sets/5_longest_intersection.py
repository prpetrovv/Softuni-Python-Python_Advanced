N = int(input())
longest_intersection = {}
for _ in range(N):
    first, second = input().split('-')
    first_start, first_end = tuple(map(int, first.split(',')))
    second_start, second_end = tuple(map(int, second.split(',')))
    first_set = {num for num in range(first_start, first_end + 1)}
    second_set = {num for num in range(second_start, second_end + 1)}
    intersection = first_set & second_set
    if longest_intersection:
        if len(intersection) > len(longest_intersection):
            longest_intersection = intersection
    else:
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
