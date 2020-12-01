# DFS 메소드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')     # 방문한 노드 출력
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 스택 활용한 DFS 메소드 정의
def dfs_stack(graph, visited):
    stack = [1] # 1번 노드부터 탐색

    while stack:
        v = stack.pop()

        if not visited[v]:
            visited[v] = True   # 방문 처리
            print(v, end=' ')   # 방문한 노드 출력

            stack.extend(reversed(graph[v]))


# 각 노드가 연결된 정보를 표현 (2차원 리스트)
# 노드 번호가 1부터 시작하기 때문에 편의상 0번째에는 빈 리스트 추가
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)  # 1번 노드부터 탐색 시작
print()

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9
dfs_stack(graph, visited)
