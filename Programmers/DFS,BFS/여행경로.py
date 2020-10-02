def solution(tickets):
    graph = {}
    airports = []

    for index in range(len(tickets)):
        departure, arrival = tickets[index][0], tickets[index][1]

        if departure not in airports:
            airports.append(departure)
            graph[departure] = [arrival]    # 그래프 생성
        else:
            graph[departure].append(arrival)    # 그래프 추가
            graph[departure].sort(reverse=True) # 알파벳 순 정렬

    print(graph)
    return dfs(graph, tickets)

def isEmpty(graph):
    for value in list(graph.values()):
        if value:   # 리스트가 존재한다면 비어있지 않음
            return False
    return True


def dfs(graph, tickets):  # N은 티켓수
    visited = []
    start = "ICN"
    need_visit = [start]

    while not isEmpty(graph):
        print(need_visit)
        for i in range(len(need_visit)-1, -1, -1):
            if need_visit[i] in list(graph.keys()) :
                node = need_visit[i]
                del need_visit[i]
                break
        else:
            visited.append(need_visit.pop())
            break
       
        if len(visited) >= 2 and visited[-2] in list(graph.keys()):
            graph[visited[-2]].pop()    # 이전에 방문한 거 제거해줌 
        
        visited.append(node)
        need_visit.extend(graph[node])

    return visited

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"] ]))
print(solution([["ICN", "SFO"], ["SFO", "AAD"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))