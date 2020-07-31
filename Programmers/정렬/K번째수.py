# 내가 푼 방법
def solution(array, commands):
    answer = []

    # i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, 
    # k번째에 있는 수를 구함
    for i, j, k in commands:
        arr = sorted(array[i-1:j])
        answer.append(arr[k-1])
    return answer

# 해결 방법1
def solution1(array, commands):
    # lambda parameters : expression
    return list(map(lambda x : sorted(array[x[0]-1 : x[1]])[x[2]-1], commands))


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
print(solution1(array, commands))