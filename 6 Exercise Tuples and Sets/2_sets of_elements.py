n, m = [int(x) for x in input().split(" ")]
n_set = set()
m_set = set()
for _ in range(n):
    n_set.add(int(input()))

for _ in range(m):
    m_set.add(int(input()))
both = m_set.intersection(n_set)
for number in both:
    print(number)
