number = int(input())
my_stack = list()
for i in range(number):
    command = input().split()
    if len(command) > 1:
        my_stack.append(int(command.pop()))
    else:
        if my_stack:
            command = int(command.pop())
            if command == 2:
                my_stack.pop()
            elif command == 3:
                print(max(my_stack))
            elif command == 4:
                print(min(my_stack))
        else:
            continue
reversed_stack = list()
while my_stack:
    reversed_stack.append(my_stack.pop())
print(", ".join(str(x) for x in reversed_stack))