import copy

n = int(input())
triangle = []
for _ in range(n):
    array = list(map(int, input().split()))
    triangle.append(array)

# DP 테이블 초기화
dp = copy.deepcopy(triangle) 
for i in range(1, n):   # 두번째 줄부터 시작
    for j in range(len(dp[i])):
        # 왼쪽 위에서 오는 경우
        if j-1 >= 0:
            left_up = dp[i-1][j-1]
        else:
            left_up = -1    # 값이 없음
        
        # 오른쪽 위에서 오는 경우
        if j < len(dp[i-1]) :
            right_up = dp[i-1][j]
        else:
            right_up = -1   # 값이 없음
        
        dp[i][j] += max(left_up, right_up)

print(max(dp[-1]))