def solution(nums):
    answer = 0
    n = len(nums)//2
    # nums에 존재하는 폰캣몬의 종류
    count = len(set(nums))
    
    if n <= count:
        # 매번 새로운 종류를 고를 수 있는 경우
        return n
    
    # 최대 종류의 수
    return count

print(solution([3,1,2,3]))