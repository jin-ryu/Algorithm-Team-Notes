import heapq

# 도시의 개수, 통로의 개수, 메시지를 보내고자 하는 도시
n, m, c = map(int, input().split())
# 통로 정보를 저장하는 리스트
graph = [[] for i in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# 최단 거리를 저장하는 리스트
INF = int(1e9)
distance = [INF] * (n+1)

# 다익스트라 알고리즘 활용
def dijkstra(start):
    q = []
    # 시작 노드의 최단 거리는 0으로 설정
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 이미 최단 거리가 정해진 경우 무시
        if distance[now] < dist:
            continue
        # 인접한 노드들을 탐색
        for i in graph[now]:
            cost = dist + i[1]  # 현재 노드를 지나서 가는 경우 비용
            if cost < distance[i[0]]:
                # 현재 노드를 지나서 가는 비용이 더 적은 경우 갱신
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# c에서 각 노드로 가는 최단 거리 계산
dijkstra(c)

# 결과 출력
count, time = 0, 0
for i in range(1, n+1):
    if i != c and distance[i] != INF:
        count += 1
        time = max(time, distance[i])

print(count, time)






