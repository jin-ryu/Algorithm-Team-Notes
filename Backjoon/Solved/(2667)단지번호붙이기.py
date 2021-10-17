N = int(input())
board = [input() for _ in range(N)]

V = []    # 전체 방문 리스트
result = []

def find(i, j):
    global N, board
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    stack = [(i, j)]
    visited = []
    
    while stack:
        x, y = stack.pop()
        if (x, y) not in visited:
            visited.append((x, y))

            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]

                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] == '1' and (nx, ny) not in visited:
                        stack.append((nx, ny))

    return visited

for i in range(N):
    for j in range(N):
        if board[i][j] == '1' and (i, j) not in V:
            v = find(i, j)
            result.append(len(v))
            V.extend(v)

result.sort()
print(len(result))
for r in result:
    print(r)
            