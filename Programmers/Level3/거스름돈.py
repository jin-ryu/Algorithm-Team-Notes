def solution(n, money):
    # dp[y][x] = y종류의 money로 x원을 만드는 방법의 수
    dp = [[0 for _ in range(n+1)] for _ in range(len(money))]
    # 어떤 화페를 쓰든 0원을 돌려주는 방법은 1가지 (나머지 0원이 따라옴)
    dp[0][0] = 1  
    
    # 동전의 최소값으로 만들 수 있는 경우 채움 (나머지 경우는 만들 수 없음)
    for i in range(money[0], n+1, money[0]):
        dp[0][i] = 1
    
    # 점화식 = y-1종류로 이미 x원을 만든 경우 + y를 무조건 하나이상 사용하고 차액을 y종류로 만든 경우
    # dp[y][x] = dp[y-1][x] + dp[y][x-money[y]]
    for y in range(1, len(money)):
        for x in range(n+1):
            if x >= money[y]:
                # y원을 새로 사용할 수 있는 경우 dp 갱신
                dp[y][x] = (dp[y-1][x] + dp[y][x-money[y]]) % 1000000007
            else:
                # 아닌 경우는 이전 dp값과 동일
                dp[y][x] = dp[y-1][x]

    return dp[-1][-1]

print(solution(5, [1,2,5]))