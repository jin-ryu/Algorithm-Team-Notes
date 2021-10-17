n, k = map(int, input().split())
arr = list(map(int, [input() for _ in range(n)]))
dp = [10001] * (k+1)    # dp[k] : 숫자 k를 만들기 위한 최소 숫자 개수

dp[0] = 0    
for i in arr:
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i] + 1)

if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])