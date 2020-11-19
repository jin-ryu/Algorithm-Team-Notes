def solution(n):
    sqrt = n**(1/2)
    
    if sqrt % 1 == 0:   # 정수인지 확인
        return (sqrt+1)**2
    
    return -1