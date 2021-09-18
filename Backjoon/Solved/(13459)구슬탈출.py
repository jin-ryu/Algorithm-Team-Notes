from sys import stdin
from collections import deque
input = stdin.readline

# 입력
n, m = map(int, input().split())
board = []
rx, ry, bx, by = [0]*4
for i in range(n):
    board.append(input())
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

def move(x, y, _dx, _dy, cnt):
    while board[x+_dx][y+_dy] != '#' and board[x][y] != 'O':
        x += _dx
        y += _dy
        cnt += 1
    return (x, y, cnt)

def bfs():
    q = deque([(rx, ry, bx, by, 0)]) # red, blue, depth
    visited[rx][ry][bx][by] = True

    while q:
        _rx, _ry, _bx, _by, depth = q.popleft()
        if depth >= 10:
            break

        for i in range(4):
            nrx, nry, rc = move(_rx, _ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(_bx, _by, dx[i], dy[i], 0)

            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                return 1

            if (nbx, nby) == (nrx, nry):
                if rc < bc:
                    nbx -= dx[i]
                    nby -= dy[i]
                else:
                    nrx -= dx[i]
                    nry -= dy[i]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, depth+1))

    return 0

print(bfs())


