from itertools import product

def solution(numbers):
    answer = []
    # 짝수의 경우 맨 뒤 비트가 항상 0이므로 이를 1로 반전
    # 홀수의 경우 뒤에서 가장 가까운 0을 1로 바꾸고 그 아래 1중 가장 큰 1을 0으로 반전

    for num in numbers:
        # 비트 크기를 계산하거나 앞에 무조건 0을 붙이기
        n = bin(num)[2:].zfill(50)
        li = list(n)
        
        # 맨 뒤 0을 1로 바꿔줌
        i = n.rfind('0')
        li[i] = '1'
        
        if num % 2 == 1:
            # 홀수이면 i 뒤의 1을 0으로 반전
            li[i+1] = '0'
            
        answer.append(int(''.join(li), 2))
            
            
    return answer