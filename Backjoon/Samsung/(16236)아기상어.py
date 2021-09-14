from collections import deque
from sys import stdin
input = stdin.readline

# 입력
n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
X, Y = 0, 0         # 아기 상어의 위치
size = 2            # 아기 상어의 크기

# 초기화
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            X, Y = i, j
            space[i][j] = 0

 
# 위 > 왼쪽 우선순위 반영
dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)


q = deque([(X,Y,0)])
visited = [(X, Y)]
cnt = 0
answer = 0


print()
while q:
    x, y, depth = q.popleft()

    if space[x][y] != 0 and space[x][y] < size:
        # 먹을 수 있는 물고기가 있다면 먹는다
        space[x][y] = 0
        cnt += 1

        if size == cnt:
            # 아기 상어 크기 증가
            size += 1
            cnt = 0    

        # 새로운 위치에서 탐색을 시작할 수 있게 큐를 비워줌
        q = deque([(x, y, 0)])
        visited = [(x, y)]
        print(x, y)
        for i in range(n):
            print(space[i])
        #print(size, cnt)
        #print(q)

        # 물고기를 먹었을 때의 시간을 더해줌
        answer += depth
        print(answer)
        continue

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
            if space[nx][ny] <= size:
                # 지나갈 수 있는 칸이면 지나간다.
                q.append((nx, ny, depth+1))
                visited.append((nx, ny))
    print(q)

print(answer)