s = set(["ABC", "ARC", "AGC", "AHC"])
for _ in range(3):
    i = input()
    s.discard(i)

for e in s:
    print(e)