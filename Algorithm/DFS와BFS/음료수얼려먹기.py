def search(board, start, visited):
    direction = [(-1,0), (1,0), (0,-1), (0,1)]
    group = [start]
    result = []

    while group:
        x, y = group.pop()
        visited[x][y] = True    # 방문 처리
        result.append((x,y))

        # 상하 좌우 탐색
        for d in direction:
            # 이동
            i = x + d[0]
            j = y + d[1] 

            # 범위를 벗어나거나 이미 방문했던 경우 제외
            if (0 > i or i >= N) or (0 > j or j >= M) or visited[i][j]:
                continue

            if board[i][j] == 0 and (i,j) not in group:
                group.append((i,j))

    print(result)

    return visited


N, M = map(int, input().split())
board = []
for _ in range(N):
    line = list(map(int, input()))
    board.append(line)

visited = [[False] * M for _ in range(N)]  # 방문 여부 저장
count = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and not visited[i][j]:
            start = (i,j)
            visited = search(board, start, visited)
            count += 1

print(count)


