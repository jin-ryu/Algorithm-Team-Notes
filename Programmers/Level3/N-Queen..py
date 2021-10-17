def solve(board, row):
    # board[i] : i번째 row에서 Queen의 위치    
    n = len(board)
    result = 0
    
    if row == n:
        return 1
    
    for col in range(n):
        board[row] = col    # Queen 배치
        
        for i in range(row):
            # 이전 경우에서 만족하지 않는 조건이 있는 경우 제외
            if board[row] == board[i]:
                # 같은 col에 있는 경우 
                break
            if row - i == abs(board[row] - board[i]):
                # 기울기 절대값이 1인 경우 대각선에 있는 것
                break
                
        else:
            # Queen을 배치하는 조건에 맞는 경우 다음 row 탐색
            result += solve(board, row+1)
            
    return result
        
        
def solution(n):
    
    return solve([0]*n, 0)