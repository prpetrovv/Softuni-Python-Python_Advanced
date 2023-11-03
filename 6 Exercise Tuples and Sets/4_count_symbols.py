text = input()
symbols = []
for s in text:
    symbols.append(s)
ordered_set = sorted(set(symbols))

for i in ordered_set:
    times = symbols.count(i)
    print(f"{i}: {times} time/s")
