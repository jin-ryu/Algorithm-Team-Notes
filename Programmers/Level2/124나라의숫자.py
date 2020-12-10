def solution(n):
    # 3진법과 유사함을 이용
    answer = ''
    
    while n > 0:
        # 3진법은 0부터 시작하지만, 124 나라는 1부터 시작
        # n-1로 몫과 나머지를 구함
        share = (n-1)//3
        remainder = (n-1)%3
        
        if remainder == 0:
            answer = "1" + answer
        elif remainder == 1:
            answer = "2" + answer
        else:
            answer = "4" + answer
      
        # n 갱신
        n = share 
        
    return answer


print(solution(1))  # 1
print(solution(2))  # 2
print(solution(3))  # 4
print(solution(4))  # 11
print(solution(10))  # 41
