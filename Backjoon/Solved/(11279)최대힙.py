import sys
import heapq

N = int(sys.stdin.readline())

h= []
for _ in range(N):
    v = int(sys.stdin.readline())
    if v > 0:
        heapq.heappush(h, -v)
    elif v == 0:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)