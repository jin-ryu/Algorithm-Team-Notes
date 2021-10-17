def solution(gems):
    answer = []
    start, end = 0, 0
    now = {}
    types = set(gems)
    min_value = len(gems)
    
    while end < len(gems):
        # end를 끝까지 탐색하지 않았다면 반복
        while end < len(gems) and len(now.keys()) != len(types):
            # 조건에 맞을 때까지 end 증가
            if gems[end] not in now.keys():
                now[gems[end]] = 1
            else:
                now[gems[end]] += 1
            end += 1
        
        while start <= end and len(now.keys()) == len(types):
            # 조건에 맞을 때까지 start 증가
            now[gems[start]] -= 1
            if now[gems[start]] == 0:
                del now[gems[start]]
            start += 1 

        if end - start < min_value:
            # 최소 구간이면 갱신
            answer = [start, end]
            min_value = end - start
        
        
    return answer