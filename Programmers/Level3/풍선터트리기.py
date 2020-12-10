import copy

def solution(a):
    # dp 활용
    answer = len(a)
    left = copy.deepcopy(a)  
    right = copy.deepcopy(a)
    
    for i in range(1, len(a)):
        # 왼쪽에서 i번째까지 최소값
        left[i] = min(left[i-1], left[i])
    
    for i in range(len(a)-2, -1, -1):
        # 오른쪽에서 i번재까지 최소값
        right[i] = min(right[i+1], right[i])
        
    for i in range(1, len(a)-1):
        # 양 끝값은 무조건 남을 수 있으므로 제외
        if a[i] > left[i-1] and a[i] > right[i+1]:
            # i번째 값이 양옆의 최소값보다 크면 마자믹까지 남을 수 없음
            answer -= 1
        
        
    return answer

#  -16, -92, -71, -68, -61, -33
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))