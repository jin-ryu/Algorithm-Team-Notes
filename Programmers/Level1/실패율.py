# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 개수 N
# 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages

def solution(N, stages):
    failure = {}    # 스테이지에 따른 실패율 저장
    
    for stage in range(1, N+1):
        # 실패율 계산
        reach = len([s for s in stages if s >= stage])
        not_clear = stages.count(stage)
        if reach != 0:
            fail_rate =  not_clear / reach
        else:
            fail_rate = 0   #  스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0
        failure[stage] =  fail_rate
    
    # 실패율로 정렬, 같은 실패율이면 스테이지 번호로 정렬
    failure = dict(sorted(failure.items(), key=lambda x: (-x[1], x[0])))   

    return list(failure.keys())

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4])) # [4,1,2,3]
