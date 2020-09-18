def solution(routes):
    answer = 0
    visited = [0]*len(routes)

    routes.sort()   # 시작 지점으로 정렬

    # 첫번재 구간 방문
    visited[0] = 1
    answer += 1
    start, end = routes[0][0], routes[0][1]

    while sum(visited) != len(routes):
        for idx in range(1, len(routes)):
            if start <= routes[idx][0] <= end:    # 겹치는 구간이 있다면
                visited[idx] = 1
                # 새로운 겹치는 구간 설정
                if routes[idx][0] > start:    
                    start = routes[idx][0]
                if routes[idx][1] < end:
                    end = routes[idx][1]
            else:   # 더 이상 겹치는 구간이 안나오면 새로운 구간으로 탐색
                start, end = routes[idx][0], routes[idx][1]
                visited[idx] = 1
                answer += 1
    
    return answer

def solution2(routes):
    routes = sorted(routes, key=lambda x: x[1]) # 종료지점으로 정렬
    last_camera = -30000    # 도로의 최소 값
    answer = 0

    for route in routes:
        # 시작 지점이 마지막 카메라가 있는 지점보다 크다면
        # 카메라가 해당 구간을 지나가는 차를 못봄
        if last_camera < route[0]:
            answer += 1     # 카메라 추가
            last_camera = route[1]  # 카메라 위치는 해당 구간의 마지막 위치
 
    return answer

print(solution2([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))   # 2