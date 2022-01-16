import sys
import bisect

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

temp = []
for n in arr:
    if not temp or temp[-1] < n:
        temp.append(n)
    else:
        i = bisect.bisect_left(temp, n)
        temp[i] = n     # lower_bound를 찾아 값 교체

print(len(temp))