N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def backtacking(now, arr):
    if len(now) == M:
        # 결과 출력
        print(' '.join(map(str, now)))
        return

    for i in range(N):
            now.append(arr[i])
            backtacking(now, arr)
            now.pop()


backtacking([], arr)