n, k = map(int, input().split())
arr = list(map(int, [input() for _ in range(n)]))
dp = [0] * (k+1)    # dp[k] : 숫자 k를 만들기 위한 경우의 수

dp[0] = 1    # 숫자 추가할 때 경우의 수 추가하기 위해 1로 설정
for i in arr:
    for j in range(i, k+1):
        # dp[j] : dp[j-i] 까지 경우의 수에 각각 i씩 더해주면 만들 수 있음
        dp[j] += dp[j-i]
    
print(dp[-1])