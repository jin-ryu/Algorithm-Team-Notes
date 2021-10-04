N, M = map(int, input().split())
arr = list(map(int, input().split()))
isUsed = [False for i in range(N)]

answer = []
def backtacking(now, arr, isUsed, answer):
    if len(now) == M:
        # 결과 담기
        answer.append(tuple([i for i in now]))
        return

    for i in range(len(arr)):
        if not isUsed[i]:
            now.append(arr[i])
            isUsed[i] = True

            backtacking(now, arr, isUsed, answer)
            
            now.pop()
            isUsed[i] = False

backtacking([], arr, isUsed, answer)
answer = sorted(list(set(answer)))

for i in range(len(answer)):
    for j in range(len(answer[0])):
        print(answer[i][j], end=" ")
    print()