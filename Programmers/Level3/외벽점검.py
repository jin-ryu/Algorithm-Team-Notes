from itertools import permutations

def solution(n, weak, dist):
    size = len(weak)
    # 원형 배열을 2배로 늘려줌 (시계, 반시계 문제 해결)
    weak += [n+i for i in weak]
    
    # 투입할 수 있는 친구의 최댓값
    answer = len(dist) + 1
    orders = permutations(dist, len(dist))
    for order in orders:
        # 투입하는 친구 순서를 변경하며 탐색
        for start in range(size):
            # 탐색 시작 위치를 변경하며 탐색
            count = 0
            coverage = weak[start] + order[count]
            for idx in range(start, start+size):
                # 취약 지점의 위치를 탐색
                if coverage < weak[idx]:
                    # 다 커버하지 못하는 경우 친구 추가
                    count += 1
                    if count >= len(order):
                        # 모든 친구를 투입해도 불가능한 경우 
                        break
                    # coverage 갱신
                    coverage = weak[idx] + order[count]
            # 최소 친구 수 갱신
            answer = min(answer, count+1)
    
    if answer > len(dist):
        # 친구들을 모두 투입해도 점검할 수 없는 경우
        return -1
        
    return answer

print(solution(200, [0, 100], [1, 1]))