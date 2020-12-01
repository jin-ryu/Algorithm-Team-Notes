# DP 문제
def solution(board):
    answer = 0
    # 정사각형이 되는 경우: 위, 대각선, 옆(왼쪽)의 값이 0이 아닐때
    # 정사각형이 될 가능성이 있는 것에 +1
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] >=  1:
                # 1보다 클 때만 업데이트
                # 모두가 1이상이라면 2로 업데이트 = 2x2 정사각형
                board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1
    
    # board의 결과: 오른쪽 하단의 숫자가 만들 수 있는 최대 정사각형의 변의 길이
    for i in range(len(board)):
        answer = max(answer, max(board[i]))

    return answer**2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))  # 9
print(solution([[0,0,1,1],[1,1,1,1]]))  # 4