def solution(n):
    answer = ''
    indices = 1
    
    while n / 3**indices > 1:
        indices += 1
    

    return answer

print(solution(1))  # 1
print(solution(2))  # 2
print(solution(3))  # 4
print(solution(4))  # 11
