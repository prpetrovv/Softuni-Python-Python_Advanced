from collections import deque

pumps = int(input())
petrol_refills = deque()
distances_from = deque()

for p in range(pumps):
    info = [int(x) for x in input().split()]
    distances_from.append(info.pop())
    petrol_refills.append(info.pop())

for i in range(pumps):
    petrol = 0
    edit_petrol_ref = petrol_refills.copy()
    edit_distance = distances_from.copy()
    edit_distance.rotate(-i)
    edit_petrol_ref.rotate(-i)
    flag = True
    for j in range(pumps):
        petrol += edit_petrol_ref.popleft()
        c_distance = edit_distance.popleft()
        if petrol >= c_distance:
            petrol -= c_distance
        else:
            flag = False
            break
    if flag:
        print(i)
        break
