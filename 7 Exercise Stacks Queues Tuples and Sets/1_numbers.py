first = set(input().split(' '))
second = set(input().split(' '))
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0:2] == ['Add', 'First']:
        command = command[2::]
        first = first.union(command)
    elif command[0:2] == ['Add', 'Second']:
        command = command[2::]
        second = second.union(command)
    elif command[0:2] == ['Remove', 'First']:
        command = command[2::]
        for i in command:
            if i in first:
                first.remove(i)
    elif command[0:2] == ['Remove', 'Second']:
        command = command[2::]
        for i in command:
            if i in second:
                second.remove(i)
    else:
        if first.issubset(second) or second.issubset(first):
            print(True)
        else:
            print(False)
print(', '.join(map(str, (sorted(map(int, first))))))
print(', '.join(map(str, (sorted(map(int, second))))))
