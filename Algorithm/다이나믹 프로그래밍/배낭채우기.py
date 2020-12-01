from itertools import combinations

class Solution:
    def knapsack(self, w, v, k):
        n  = len(w)
        # dp[i][j] = 처음부터 i번째 보석까지 무게 j를 가지면서 얻을 수 있는 최대 이익
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            # i: 보석 번호
            for j in range(1, k+1):
                # j: 현재 배낭 무게
                if w[i-1] > j :
                    # i번째 보석이 현재 배낭 무게보다 무거울 경우 전단계 최적값을 가져온다
                    dp[i][j] = dp[i-1][j]
                else:
                    # 아닌 경우 i번째 보석만큼 무게를 비웠을 때의 최적값 + i번째 보석의 가치와 전단계의 최적값 중 큰 값을 가져온다
                    dp[i][j] = max(dp[i-1][j-w[i-1]]+v[i-1], dp[i-1][j])
       
        return dp[n][k]

a = Solution()
print(a.knapsack([10,20,30,40], [60,100,120,200], 50))