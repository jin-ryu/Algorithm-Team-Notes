def solution(num):
    answer = 0
    for i in range(500):
        # 입력값이 1인 경우를 고려해서 반복문 상단에 위치해야함
        # 입력된 수의 범위 잘 보기
        if num == 1:
            return answer  
        
        if num%2 == 0:
            num /= 2
        else:
            num = 3*num +1
        answer += 1
        
    return -1