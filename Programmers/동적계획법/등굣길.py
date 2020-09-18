# 최단거리로 가는 방법: 왼쪽 혹은 위에서 오는 것
# 동적 계획법(DP): 해당 위치의 최단거리 경우의 수 = 왼쪽 칸의 경우의 수 + 위쪽 칸의 경우의 수
def solution(m, n, puddles):    
    route = [[0]*(m+1)]*(n+1)   # (1,1)부터 시작하므로 (m+1)x(n+1) 크기 배열 선언
    route[1][1] = 1             # (1,1)에서 (1,1)로 가는 방법은 제자리에 있는 것 
    for i in range(1, n+1):
        for j in range(1, m+1): 
            if i==1 and j==1:
                continue   
            elif [j,i] in puddles:    # 가로, 세로가 우리가 아는 인덱스와 반대이므로 [j,i]
                route[i][j] = 0     # 물 웅덩이를 지나가는 경우는 없으므로 0으로 둠
            else:
                route[i][j] = route[i-1][j] + route[i][j-1]     # 해당 위치의 최단거리 경우의 수 = 왼쪽 칸의 경우의 수 + 위쪽 칸의 경우의 수
    

    return route[-1][-1] % 1000000007

print(solution(4, 3, [[2, 2]])) # 4