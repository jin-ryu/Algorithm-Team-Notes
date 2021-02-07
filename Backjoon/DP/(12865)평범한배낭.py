# 데이터 입력
n, k = map(int, input().split())
weights, values = [], []
for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# dp[i][j]: i번째 물품까지 고려했을 때 j무게에서 얻을 수 있는 가치의 최댓값
dp = [[0 for j in range(k+1)] for i in range(n)]
for i in range(n):
    for j in range(1, k+1):
        if weights[i] > j:
            # i번째 물품의 무게가 현재 가방의 무게보다 크면 이전 결과 반영
            dp[i][j] =  dp[i-1][j]
        else:
            # i번재 물품을 추가할 수 있다면 추가하는 것과 추가하지 않는 것 중 큰 것 반영
            # dp[i-1][j]: 추가하지 않는 경우
            # dp[i-1][j-weights[i]] + values[i]: 추가하는 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])

print(dp[n-1][k])