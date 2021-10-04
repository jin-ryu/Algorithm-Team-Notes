N, M = map(int, input().split())
arr = list(map(int, input().split()))
isUsed = [False for i in range(N)]
arr.sort()

def backtacking(start, now, arr, isUsed):
    if len(now) == M:
        # 결과 출력
        print(' '.join(map(str, now)))
        return

    for i in range(start, N):
        if not isUsed[i]:
            now.append(arr[i])
            isUsed[i] = True

            backtacking(i+1, now, arr, isUsed)

            now.pop()
            isUsed[i] = False


backtacking(0, [], arr, isUsed)