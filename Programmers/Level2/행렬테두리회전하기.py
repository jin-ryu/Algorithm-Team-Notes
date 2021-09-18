def rotate(board, x1, y1, x2, y2):    
    i, j = x1, y1
    arr = [board[i][j]]
    j += 1
    
    while j < y2:   # right
        arr.append(board[i][j])
        board[i][j] = arr[-2]
        j += 1
        
    while i < x2:   # down
        arr.append(board[i][j])
        board[i][j] = arr[-2]
        i += 1
    
    while j > y1:   # left
        arr.append(board[i][j])
        board[i][j] = arr[-2]
        j -= 1
            
    while i > x1:   # down
        arr.append(board[i][j])
        board[i][j] = arr[-2]
        i -= 1
        
    board[i][j] = arr[-1]

        
    # 회전 숫자 중 최소값 반환
    return min(arr)


def solution(rows, columns, queries):
    answer = []
    # 행(row), 열(coulumn) -> i, j 
    board = [[(i-1) * columns + j for j in range(columns+1)] for i in range(rows+1)]
    
    # 회전 수행
    for x1, y1, x2, y2 in queries:
        answer.append(rotate(board, x1, y1, x2, y2))
            
    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))