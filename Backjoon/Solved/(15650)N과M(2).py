N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
isUsed = [False for i in range(1, N+1)]     # 사용여부를 체크하는게 중복 제거 역할

def backtracking(now, start, numbers, isUsed):
    if len(now) == M: 
        # 결과 출력
        print(' '.join(map(str, now)))
        return

    for i in range(start, len(numbers)):
        # 오름차순 조건 추가
        if not isUsed[i]:
            isUsed[i] = True
            now.append(numbers[i])

            backtracking(now, i+1, numbers, isUsed)

            isUsed[i] = False
            now.pop()

backtracking([], 0, numbers, isUsed)
