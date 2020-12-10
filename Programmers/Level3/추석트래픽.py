def second(time):
    # 시분초를 ms(소수점아래 셋째자리)단위로 환산
    h, m, s = map(float, time)
    return int((h*(60**2) + m*60 + s)*1000)

def count(start, times):
    # 1초의 구간동안 처리량 확인
    end = start + 1000 
    count = 0
    for s, e in times.values():
        if not (s >= end or e < start):
            # 범위 안에 한쪽 끝이라도 포함되면 카운트
            count += 1
    return count
        
def solution(lines):
    answer = 0
    times = {}
    
    for i in range(len(lines)):
        line = lines[i].split()
        # 구간 시작 시간 
        time = line[1].split(":")
        time = second(time)
        # 구긴 지속 시간
        t = int(float(line[2][:-1]) * 1000)
        # 구간 추가 (시작 시간, 끝시간)
        times[i] = [time-t+1, time]

    for i in range(len(lines)):
        # 구간 시작 시간부터 1초 탐색
        answer = max(answer, count(times[i][0], times))
        # 구간 종료 시간부터 1초 탐색
        answer = max(answer, count(times[i][1], times))
        
    return answer

# 1
print(solution(	["2016-09-15 00:00:00.000 3s"]))    
# 7
print(solution(	["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))