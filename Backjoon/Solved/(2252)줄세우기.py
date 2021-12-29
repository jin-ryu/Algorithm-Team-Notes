from collections import deque

N, M = map(int, input().split())
graph = {}
indegree = [0] * (N+1)

# 그래프 초기화
for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    l, r = map(int, input().split())
    graph[l].append(r)
    
    indegree[r] += 1


queue = deque([])

# 진입차수 0인 노드 삽입
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    n = queue.popleft()
    print(n, end=" ")

    for i in graph[n]:
        indegree[i] -= 1
        # 새롭게 진입차수 0인 노드 삽입
        if indegree[i] == 0:
            queue.append(i)
        