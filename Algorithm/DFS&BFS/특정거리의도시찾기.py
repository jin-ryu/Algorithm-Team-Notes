# PyPy3로 해야 통과 됨
# 정답 코드 참고함
from collections import deque

n, m, k, x = map(int, input().split())

# 그래프 초기화 (빈 문자열을 추가하고 싶을 때는 반복문이 픽수)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

# bfs 사용
queue = deque([x])
distance = [-1 for _ in range(n+1)]      # 도시별별 최단 거리 
distance[x] = 0     # 출발 도시까지의 거리는 0

while queue:
    v = queue.popleft()
    
    for i in graph[v]:  # 인접 도시 탐색
        if distance[i] == -1:    # 한번도 방문하지 않은 도시라면 최단거리 갱신
            distance[i] =  distance[v] + 1
            queue.append(i)

result = [i for i in range(1, n+1) if distance[i] == k]

if result:
    for r in result:
        print(r)
else:   
    print(-1)   # 도시가 하나도 존재하지 않는 경우 -1

