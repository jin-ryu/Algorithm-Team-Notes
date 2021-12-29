from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
directions = {
    0 : (-1, 0),    # up
    1 : (1, 0),     # down
    2 : (0, -1),    # left
    3 : (0, 1)      # right
}
cctv = {
    1 : [[0], [1], [2], [3]],
    2 : [[0, 1], [2, 3]],
    3 : [[0, 2], [0, 3], [1, 2], [1, 3]],
    4 : [[0, 2, 3], [1, 2, 3]],
    5 : [[0, 1, 2, 3]]
}

def find(board, visited, x, y, d):
    for i in range(d):
        dx, dy = directions[i]
        nx, ny = x+dx, y+dy
        while 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6 and board[nx][ny] not in visited:

            nx += dx
            ny += dy



for i in range(N):
    for j in range(M):
        if board[i][j] in range(1, 6):
            for k in cctv[board[i][j]]:
