import heapq

def solution(N, road, K):
    answer = 0
    graph = {}
    distance = [500001 for _ in range(N+1)]   # 최단 거리 테이블
    q = []  # 방문할 노드
    
    for a, b, c in road:
        if a in graph.keys():
            graph[a].append((b, c))  # 노드, 거리
        else:
            graph[a] = [(b, c)]

        if b in graph.keys():
            graph[b].append((a, c))  # 노드, 거리
        else:
            graph[b] = [(a, c)]
            
    # dijkstra
    heapq.heappush(q, (0, 1))   # (거리, 노드)
    distance[1] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            # 현재 최단 경로보다 더 큰 경로라면 무시
            continue
            
        for i in graph[now]:
            # 인접한 노드에 갈때 now를 거쳐가는 것이 더 짧은 경우 갱신
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    print(distance)
    print(len(list(filter(lambda x : x <= K, distance))))
        
    
    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))