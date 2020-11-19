def solution(phone_number):
    phone_number = list(phone_number)
    N = len(phone_number)
    for i in range(N):
        if i < N-4:
            phone_number[i] =  '*'
    return "".join(phone_number)

# 좋은 예시
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]  
