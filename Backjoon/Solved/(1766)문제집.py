import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

graph = {}
indegree = [0] * (N+1)
for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    l, r = map(int, sys.stdin.readline().split())
    graph[l].append(r)
    indegree[r] += 1

h = []  # 우선순위 큐 사용해서 위상정렬
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(h, i)

while h:
    v = heapq.heappop(h)
    print(v, end=" ")

    for i in graph[v]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(h, i)
