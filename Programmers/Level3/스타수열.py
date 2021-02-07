from collections import Counter

# 부분 집합을 전부다 구하면 시간초과 나는 문제!
def solution(a):
    answer = 0
    counter = Counter(a)
    
    # 배열에 등장한 횟수가 스타수열의 길이가 될 확률이 있음
    for common, count in Counter(a).items():
        if count <= answer:
            # 현재 최대 값보다 길이가 짧은 경우 패스
            continue
            
        common_count = 0   
        idx = 0
    
        while idx < len(a)-1:
            if (a[idx] == a[idx+1]) or (a[idx] != common and a[idx+1] != common):
                # 스타 수열이 아닌 경우 다음 원소 탐색
                # 집합 내 같은 원소가 있는 경우 or 교집합 원소를 포함하지 않는 경우
                idx += 1
            else:
                # 스타 수열에 위배되지 않는 경우 추가
                common_count += 1
                # 다음 원소 탐색
                idx += 2
                
        # 최대 원소 길이 갱신
        answer = max(answer, common_count)
                
    # 최대 원소 길이 * 2 = 전체 길이
    return answer * 2