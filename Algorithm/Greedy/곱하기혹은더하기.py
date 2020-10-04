def solution(S):
    answer = int(S[0])

    for index in range(1, len(S)):
        number = int(S[index])
        if number == 0 or number == 1 or answer == 0 or answer == 1: # 0 또는 1이면 더하기가 유리
            answer += number
        else:   # 나머지 경우는 곱하기가 유리
            answer *= number
    
    return answer

# 정답 코드
def answer():
    data = input()

    # 첫 번째 문자를 숫자로 변경하여 대입
    result = int(data[0])
    
    for i in range(1, len(data)):
        # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
        num = int(data[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num

    print(result)


print(solution('02984'))    # 576
print(solution('576'))    # 210
answer()