from collections import deque
from collections import deque
from sys import stdin
input = stdin.readline

# 입력
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
result = 0
q = deque()

def get(i, j):
    if board[i][j] != 0:
        q.append(board[i][j])
        board[i][j] = 0

# 합치기
def merge(i, j, _dx, _dy):
     while q:
        # 움직이려는 블록 값을 가져옴
        b = q.popleft() 

        # 빈칸인 경우 배치
        if board[i][j] == 0:
            board[i][j] = b

        # 같은 값이면 합치고 다음 인덱스로 넘어감
        elif board[i][j] == b: 
            board[i][j] = b*2 
            i, j = i+_dx, j+_dy 

        # 다른 값이면 다음 인덱스에 배치
        else:
            i, j = i+_dx, j+_dy
            board[i][j] = b
        

# 이동
def move(_dx, _dy):
    if _dx == 0:
        if _dy < 0: # 왼쪽
            for i in range(n):
                for j in range(n):
                    get(i, j)
                merge(i, n-1, _dx, _dy)
                
        else:       # 오른쪽
            for i in range(n):
                for j in range(n-1, -1, -1):
                    get(i, j)
                merge(i, 0, _dx, _dy)
    
    else:
        if _dx < 0: # 아래
            for j in range(n):
                for i in range(n-1, -1, -1):
                    get(i, j)
                merge(n-1, j, _dx, _dy)
    
        else:       # 위
            for j in range(n):
                for i in range(n):
                    get(i, j)
                merge(0, j, _dx, _dy)
    
def bfs(depth):
    global board, result, n

    # 5번 이동하면 보드의 최대값과 현재 최대값을 비교하여 갱신
    if depth >= 5:
        for i in range(n):
            result = max(result, max(board[i]))
        return

    # move 함수를 호출하면 board가 변하므로 변하기 전 상태 기록 (call by object reference)
    b = [x[:] for x in board]

    for i in range(4):
        move(dx[i], dy[i])
        bfs(depth+1)
        # 재귀 호출을 마친 후 이전 상태로 되돌림
        board = [x[:] for x in b]


bfs(0)
print(result)
    