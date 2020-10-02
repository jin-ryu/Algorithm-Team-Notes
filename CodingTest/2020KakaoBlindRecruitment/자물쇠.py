# 완전 탐색
def solution(key, lock):
    space = len(key)-1              # lock에서 상하좌우로 space만큼 키워 board 만듦
    N = len(lock) + (space)*2       # lock과 key가 겹치는 부분을 체크할 board 크기

    # key를 보드에서 한칸씩 움직여가면서 맞는지 체크
    for _ in range(5):  # 회전 횟수
        for i_start in range(N-space):
            for j_start in range(N-space):
                if is_fit(N, key, lock, space, i_start, j_start):
                    return True

        key = rotate(key)   # key 회전
        
    return False

# key로 lock을 풀 수 있는지 없는지를 확인
def is_fit(N, key, lock, space, i_start, j_start):
    board = set_board(lock, N, space)     # lock과 key가 겹치는 부분을 체크할 보드
    # key 배치
    for i in range(len(key)):
        for j in range(len(key)):  
            if key[i][j] and board[i+i_start][j+j_start]:  # 쇠의 돌기와 자물쇠의 돌기가 만나서는 안됨 (조건 빼먹음)
                return False
            board[i+i_start][j+j_start] = key[i][j] or board[i+i_start][j+j_start]   # or연산으로 홈을 매꿈
    
    # lock을 풀 수 있는지 확인
    for i in range(space, space+len(lock)):
        for j in range(space, space+len(lock)):
            if board[i][j] == 0:    # 매꾸지 못한 홈이 있음 False
                return False
    
    return True


def set_board(lock, N, space):
    # NxN board
    board = [[0]*N for _ in range(N)]

    # board 중앙에 자물쇠 배치
    for i in range(len(lock)):
        for j in range(len(lock)):
            board[i+space][j+space] = lock[i][j]
    
    return board

# key를 시계방향으로 90도 회전시키는 함수
def rotate(key):
    N = len(key)
    rotated_key = [[0]*N for _ in range(N)]

    # 회전 전의 열 번호는 회전 후의 행번호
    # 회전 후의 열은 N-1에서 회전 전의 행의 값을 뺀 것
    for r in range(N):
        for c in range(N):
            rotated_key[c][N-1-r] = key[r][c]
    return rotated_key

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])) # True
#print(solution([[1, 0, 1], [1, 0, 1], [1, 0, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]))