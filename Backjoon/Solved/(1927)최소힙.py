import sys
import heapq

N = int(sys.stdin.readline())
h = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(h, x)
    elif x == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)