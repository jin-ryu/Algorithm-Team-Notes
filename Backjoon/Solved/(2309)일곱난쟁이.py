from itertools import combinations

t = [int(input()) for i in range(9)]

result = []
comb = combinations(t, 7)
for c in comb:
    if sum(c) == 100:
        result = sorted(list(c))
        break

for r in result:
    print(r)