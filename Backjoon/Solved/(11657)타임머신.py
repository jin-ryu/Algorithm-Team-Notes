n, m = map(int, input().split())
edges = []
for _ in range(m):
    # a에서 b까지 가는 비용 c
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

INF = int(1e9)
# 최단 거리 테이블 초기화
distance = [INF] * (n+1)

def bf(start):
    # 시작 노드 방문
    distance[start] = 0
    
    for i in range(n):
        # 모든 노드에 대해서 모든 간선을 방문하며 최단 거리 갱신
        for cur, nxt, dist in edges:
            # cur을 지나 nxt에 도착하는 비용이 더 작으면 갱신
            # cur을 지나기 위해선 이미 방문한 적 있어야 함(최소 비용이 정해져 있어야 함)
            if distance[cur] != INF and distance[nxt] > distance[cur] + dist:
                distance[nxt] = distance[cur] + dist
                # 마지막 노드에 대해서도 갱신이 된다면, 음수 순환 사이클이 존재
                if i == n-1:
                    return False

    return True

if bf(1):
    # 해당 도시로 가는 최소 비용 출력
    for i in range(2, n+1):
        if distance[i] == INF: 
            # 해당 도시로 갈 수 없는 경우
            print(-1)
        else:
            print(distance[i])

else:
    # 시간을 무한히 오래 전으로 돌릴 수 있는 경우
    print(-1)


