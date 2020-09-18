def solution(n, costs):
    answer = 0
    visited = [0]*n

    costs.sort(key=lambda cost: cost[2])    # 비용에 따라 정렬

    # 첫번째 노드 방문
    visited[costs[0][0]] = 1
    visited[costs[0][1]] = 1
    answer += costs[0][2]

    while sum(visited) != n:
        print(visited)
        for cost in costs:
            start, end, weight = cost
            if visited[start] or visited[end]:
                # 비용으로 정렬해놓았기 때문에 이미 방문한 노드는 최소 비용으로 연결되어 있음
                if visited[start] and visited[end]:
                    continue
                visited[start] = 1
                visited[end] = 1
                answer += weight
                break   # 왜 꼭 break를 해야 정답인가?
                

    return answer


# [노드1, 노드2, 비용]
print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) # 4
print(solution(5, [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]])) # 7