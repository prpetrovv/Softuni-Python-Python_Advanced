n_names = int(input())
set_names = set()
for name in range(n_names):
    given_name = input()
    if given_name not in set_names:
        set_names.add(given_name)
for i in set_names:
    print(i)
