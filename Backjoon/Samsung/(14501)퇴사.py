from sys import stdin
input = stdin.readline

# 입력
n = int(input())
chart = [list(map(int, input().split())) for _ in range(n)]

# dp = i+1번째 날에 얻을 수 있는 최대 이익
dp = [0] * (n+1)

for i in range(n):
    t, p = chart[i]

    # t일 후의 최대 이익은 
    # i일에 일을 한 경우와 일을 하지 않은 경우 중 최대 값
    if i+t < n+1:
        # n+1 일에 얻을 수 있는 최대 이익을 구해야함!
        dp[i+t] = max(dp[i+t], dp[i]+p)
    
    # 다음에 있는 값보다 현재 값이 크면 다음값 갱신 (위치 상관 없음)
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[n])