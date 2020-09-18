def solution(number, k):
    current_max = number
    start = 0   # 탐색 시작하는 인덱스
    for i in range(k):  # k번 삭제
        for j in range(start, len(current_max)-1):
            if current_max[j] < current_max[j+1]:
                current_max = current_max[:j] + current_max[j+1:]
                # 이전 탐색에서 확인한 숫자들을 다시 탐색하지 않음
                if j > 0:
                    start = j-1
                break
        else:
            current_max = current_max[:-1]

    return current_max



number = "1924"
k = 2
print(solution(number, k))

number1 = "1231234"
k1 = 3
print(solution(number1, k1))

number2 = "4177252841"
k2 = 4
print(solution(number2, k2))