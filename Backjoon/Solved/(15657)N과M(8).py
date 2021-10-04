N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def backtacking(start, now, arr):
    if len(now) == M:
        # 결과 출력
        print(' '.join(map(str, now)))
        return

    for i in range(start, N):
            now.append(arr[i])
            backtacking(i, now, arr)
            now.pop()


backtacking(0, [], arr)