from sys import stdin
from collections import deque
input = stdin.readline

# 입력
n, m = map(int, input().split())
board = []
red, blue = [], []
for i in range(n):
    board.append(input())
    for j in range(m):
        if board[i][j] == 'R':
            red = [i, j]
        elif board[i][j] == 'B':
            blue = [i, j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

# 기울이기
def move(x, y, _dx, _dy, cnt):
    while board[x+_dx][y+_dy] != '#' and  board[x][y] != 'O':
        # 옆이 벽이 아니고, 현재 위치가 출구가 아닐 때 까지 기울이기
        x += _dx
        y += _dy
        cnt += 1
    return (x, y, cnt) 

# 최소 거리 구하기
def bfs():
    q = deque([(red, blue, 0)]) # red, blue, depth
    visited[red[0]][red[1]][blue[0]][blue[1]] = True

    while q:
        _red, _blue, depth = q.popleft()
        if depth >= 10:
            # 10번 초과해서 움직인 경우
            break

        for i in range(4):
            rx, ry, rc = move(_red[0], _red[1], dx[i], dy[i], 0)
            bx, by, bc = move(_blue[0], _blue[1], dx[i], dy[i], 0)

            if board[bx][by] == 'O':
                # 파란 구슬이 도착하는 경우 무시
                continue
            if board[rx][ry] == 'O':
                # 빨간 구슬이 도착
                return depth+1

            if (rx, ry) == (bx, by):
                # 빨간 구슬과 파란 구슬이 겹치는 경우, 이동 거리가 긴 것을 한칸 뒤로 보냄
                if rc < bc:
                    bx -= dx[i]
                    by -= dy[i]
                else:
                    rx -= dx[i]
                    ry -= dy[i]


            if not visited[rx][ry][bx][by]: 
                # 방문하지 않았다면 큐에 넣고 방문 처리
                q.append(([rx, ry], [bx, by], depth+1))
                visited[rx][ry][bx][by] = True

    return -1

print(bfs())