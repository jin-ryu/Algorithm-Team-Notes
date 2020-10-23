def rotate_90(m):
    # 90도 회전하는 함수
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def isMatch(board, key, start_i, start_j):
    size = len(board)
    # insert key
    for i in range(size):
        for j in range(size):
            board[start_i + i][start_j + j] += key[i][j]
             # 벽에 부딪치거나, 홈을 매꾸지 못한 경우
            if board[start_i + i][start_j + j] == 2 or 0:   
                return False

    return True
        

def solution(key, lock):
    M = len(key)
    N = len(lock)
    size = M-1+N       # board size
    board = [[1] * size for _ in range(size)] 

    # create board
    for i in range(N):
        for j in range(N):
            board[M-2+i][M-2+j] = lock[i][j]
    
    # search board
    for _ in range(4):    # 회전 반복 횟수
        for start_i in range(size-M+1):
            for start_j in range(size-M+1):

                if isMatch(board, key, start_i, start_j):
                    return True
        
        key = rotate_90(key)    # 90도 회전

    return False


# true
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# 구현 알고리즘
# 1. key를 90도씩 회전한다.
# 2. lock을 (0,0)~(N,N)까지 확인하면서 key랑 일치하는 지 확인한다
# (이때, 빈 공간이 없는지 확인한다)