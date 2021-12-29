import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# 누적합 배열 생성
sums = [0]
_sum = 0
for i in range(N):
    _sum += A[i]
    sums.append(_sum)

count = 0
s, e = 0, 1
while s <= e and e <= N:
    v = sums[e] - sums[s]
    if v < M:
        e += 1
    elif v >= M:
        s += 1
        if v == M:
            count += 1

print(count)
