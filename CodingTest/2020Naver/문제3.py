from collections import deque 

def subTree(graph, start_node, tree):   # start_node의 subTree 생성
    sub_tree = []
    for node in graph[start_node]:
        if node > start_node:   # 자기랑 연결된 하위 노드만 sub_tree에 추가
            sub_tree.append(node)

    if len(sub_tree) ==  0: # 리프 노드이면 재귀 종료
        return tree
    
    tree += sub_tree
    for i in range(len(sub_tree)):  # 다음 서브트리 방문
        tree = subTree(graph, sub_tree[i], tree)
    return tree


def bfs(graph, start_node):
    visited = deque([])
    need_visit = deque([])
    need_visit.append(start_node)	# 시작 노드 삽입
    
    while need_visit:
        # 여기서 부터
        node = need_visit.popleft()	# 리스트의 시작 원소를 방문(큐의 rear)
        if node not in visited:
            visited.append(node)

            counts = []    
            for n in graph[node]:
                counts.append(len(subTree(graph, n, [])))
            
            print(counts)
            max_index = counts.index(max(counts))  # 서브트리 개수가 가장 많은거 연결 끊음
            for n in graph[node]:
                if n != graph[node][max_index]:
                    need_visit.append(n)

            print(graph[node][max_index])
            print(visited)
    
    return list(visited)	# 노드 방문 순서

def solution(n, edges):
    graph = {}

    # 그래프 만들기
    for i in range(n):
        graph[i] = []
        for j in range(len(edges)):
            if edges[j][0] == i:
                graph[i].append(edges[j][1])
            elif edges[j][1] == i:
                graph[i].append(edges[j][0])

    bfs(graph, 0)
            
    
            


print(solution(19, [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]))