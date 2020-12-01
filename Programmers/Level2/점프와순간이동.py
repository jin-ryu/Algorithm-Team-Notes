# 특징 찾기
def solution(n):
    ans = 0
    
    # 2로 나눠떨어지게 만들어주는 것을 반복
    # 이때 나머지만큼 점프함
    while n!=0:
        if n%2 != 0:
            ans += n%2
            n = n-n%2
        else:
            n //= 2
            
    return ans

# DP로 풀 경우 효율성에서 실패
def solution2(n):
    dp = [i for i in range(n+1)]
    
    for i in range(2, n+1):
        # min(현재 내 값, 바로 전에서 점프하는 것, 순간 이동하는 것)
        # min(dp[i], dp[i-1]+1, (가능하다면)dp[i//2])
        dp[i] = min(dp[i], dp[i-1]+1)
        if i%2 == 0:
            dp[i] = min(dp[i], dp[i//2])
 
    return dp[n]
