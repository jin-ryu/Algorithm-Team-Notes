import heapq

# 전체 회사의 개수, 경로의 개수
n, m = map(int, input().split())
graph = [[] for _ in range(m+1)]
for _ in range(1, m+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 경유 회사, 도착 회사
x, k = map(int, input().split())

INF = int(1e9)
def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))    # 자기 자신한테 가는 시간은 0

    while q:
        dist, now = heapq.heappop(q)
        # 이미 방문한 회사면 무시
        if dist > distance[now]:
            continue
        # 인접한 회사들 방문
        for i in graph[now]:
            # i회사를 가기 위해 now 회사를 거쳐가는 비용
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))  # i회사로 이동
    
    return distance

# 다익스트라 알고리즘 적용
result = dijkstra(1)[k] + dijkstra(k)[x]
if result >= INF:
    print(-1)       # 도달할 수 없다면 -1 출력
else:
    print(result)
    
