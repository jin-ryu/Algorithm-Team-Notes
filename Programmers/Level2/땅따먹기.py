import copy

def solution(land):
    # i,j까지 도달하기까지 얻은 최고점
    dp = copy.deepcopy(land)
    n, m = len(land), len(land[0])

    for i in range(1, n):
        for j in range(m):
            max_num = 0
            for k in range(m):
                if k == j:
                    # 같은 열을 연속해서 밟을 수 없음
                    continue
                max_num = max(max_num, dp[i-1][k])
            dp[i][j] += max_num
    
    print(dp)
    
    return max(dp[n-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))