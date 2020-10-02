# 효율성 따져봐야함
def solution(n):
    n_str = str(n)   # 덧셈을 용이하게 하기 위해 str으로 변환
    count = 0   # 연산 횟수

    if len(n_str) == 1: # 한자리 수인 경우 덧셈기호를 삽입할 수 없으므로 그대로 반환
        return [0, n]
    
    while len(n_str) != 1:
        nums = []   # 덧셈한 결과
        for index in range(1, len(n_str)):    # 숫자와 숫자 사이를 모두 탐색

            if len(n_str) > 1 and n_str[index:].startswith("0"):    # 0을 제외한 0으로 시작하는 수는 덧셈하지 않음
                continue    
            nums.append(int(n_str[:index]) + int(n_str[index:]))
        n_str = str(min(nums))  # 가장 최소값을 가지는 덧셈 결과를 선택
        count += 1

    return [count, int(n_str)]

print(solution(73425))
print(solution(10007))
print(solution(9))