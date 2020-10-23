from collections import deque

# 문제 해결 아이디어 참고
def bfs(x, y):
    queue = deque([(x,y)])    # BFS를 구현하기 위한 큐
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):  # 상하좌우 탐색
            # 좌표 이동
            nx = x+dx[i]
            ny = y+dy[i]

            # 이동한 좌표가 미로 밖을 벗어나는 경우는 제외
            if nx < 0 or nx >= N  or ny < 0 or ny >= M:
                continue
        
            # 이동한 좌표에 괴물이 있는 경우 제외
            if maze[nx][ny] == 0:
                continue
            
            # 처음 방문하는 경우만 탐색 (방문한 좌표는 1보다 큰 수를 가지고 있을 것)
            if maze[nx][ny] == 1:    
                # 이동한 좌표는 이전 좌표에서 1만큼 이동한 것
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))  # 다음에 탐색할 좌표 삽입

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input())))

# 좌표 이동에 사용되는 값
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(0, 0)   # BFS 호출
print(maze[N-1][M-1])