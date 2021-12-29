N, S = map(int, input().split())
arr = map(int, input().split())

# 누적합 구하기
sums = [0]
value = 0
for n in arr:
    value += n
    sums.append(value)

# 부분합 구간 구하기
s, e = 0, 0
min_len = N+1

while s <= e and e <= N:
    v = sums[e]-sums[s]
    if v < S:
        e += 1
    else:
        min_len = min(min_len, e-s)
        s += 1

if min_len == N+1:
    print(0)
else:
    print(min_len)