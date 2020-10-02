# 네트워크는 dfs
def solution(n, computers):
    answer = 0
    graph = {}

    # 그래프 그리기
    for i in range(n):
        graph[i] = []
        for j in range(n): 
            # 자기 자신이 아닌 연결된 노드면 그래프에 추가
            if j != i and computers[i][j] == 1:
                graph[i].append(j)

    # dfs로 탐색
    nodes = [x for x in range(n)]
    while nodes:
        visited = dfs(graph, nodes.pop(0))
        nodes = list(set(nodes)-set(visited))
        answer += 1

    return answer

def dfs(graph, start_node):
    visited, need_visit = list(), list()	# 큐, 스택
    need_visit.append(start_node)	# 시작 노드 삽입
    
    while need_visit:
        node = need_visit.pop()	# 리스트의 끝 원소를 방문(스택 top)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])	# 다음 레벨에 있는 노드들을 need_visit에 추가
            
    return visited	# 노드 방문 순서

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))   # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))   # 1
