N = int(input())
odd_numbers = set()
even_numbers = set()
for i in range(1, N + 1):
    name_score = 0
    name = input()
    for symbol in name:
        name_score += ord(symbol)
    name_score = name_score // i
    if name_score % 2 == 1:
        odd_numbers.add(name_score)
    else:
        even_numbers.add(name_score)
sum_odds = sum(odd_numbers)
sum_even = sum(even_numbers)

if sum_odds == sum_even:
    print(', '.join(map(str, (odd_numbers - even_numbers))))
elif sum_odds > sum_even:
    print(', '.join(map(str, (odd_numbers - even_numbers))))
else:
    print(', '.join(map(str, (even_numbers ^ odd_numbers))))
