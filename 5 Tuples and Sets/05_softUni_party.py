reservations = set()
n_guests = int(input())
for guest in range(n_guests):
    reservations.add(input())

command = input()
while command != "END":
    if command in reservations:
        reservations.remove(command)
    command = input()
print(len(reservations))

vips = sorted(set(reserv for reserv in reservations if 57 >= ord(reserv[0]) >= 48))
for i in vips:
    print(i)
not_vips = sorted(i for i in reservations if i not in vips)
for i in not_vips:
    print(i)
