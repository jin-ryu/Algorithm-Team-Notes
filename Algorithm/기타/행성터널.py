n = int(input())
planet = []
for num in range(n):
    x, y, z = map(int, input().split())
    planet.append((x, y, z, num))   # 노드 번호 추가

# 간선 생성 (이때 모든 간선을 생성하면 시간초과)
edges = []
for i in range(3):
    # x, y, z 좌표 순으로 정렬
    planet.sort(key=lambda x: x[i])
    # (x1, y1) (x2, y2) (x3, y3)에서 x1-x2거리가 x1-x3보다 항상 작으므로
    # 좌표순으로 정렬했을 때 인접한 것만 간선에 넣음
    a = planet[0][3]
    for j in range(1, n):  
        # 각 좌표별로 간선 추가
        b = planet[j][3]
        cost = abs(planet[j][i]-planet[j-1][i])
        edges.append((cost, a, b)) # 비용 기준으로 정렬되게 함
        a = b   # 좌표 이동

# 크루스칼 알고리즘 사용 (최소 신장트리)
edges.sort()
parent = [i for i in range(n)]  # 부모는 자기자신으로 설정

def find_parent(parent, x):
    # 자기자신이 부모일때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 작은 노드번호 기준으로 합치기
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
for edge in edges:
    # 모든 간선을 체크하며
    cost, a, b = edge
    # 사이클이 발생하지 않는다면 최소신장트리에 넣음 
    if find_parent(parent, a) != find_parent(parent, b):
        union_find(parent, a, b)
        result += cost  # 최소 비용 계산
    

print(result)