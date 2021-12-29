import sys
import heapq

N = int(input())
h = []

for _ in range(N):
    x = int(sys.stdin.readline())   # 이거 input으로 하면 시간 초과남

    if x == 0:
        if h:
            key, value = heapq.heappop(h)
            print(value)
        else:
            print(0)

    else:
        heapq.heappush(h, (abs(x), x))
