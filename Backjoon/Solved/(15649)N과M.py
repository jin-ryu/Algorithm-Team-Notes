N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
isUsed = [False for i in range(1, N+1)]     # 사용여부를 체크하는게 중복 제거 역할

def backtracking(now, numbers, isUsed):
    if len(now) == M:
        # 결과 출력
        print(' '.join(map(str, now)))
        return
        
    for i in range(len(numbers)):
        if not isUsed[i]:
            isUsed[i] = True
            now.append(numbers[i])

            backtracking(now, numbers, isUsed)

            isUsed[i] = False
            now.pop()

backtracking([], numbers, isUsed)
