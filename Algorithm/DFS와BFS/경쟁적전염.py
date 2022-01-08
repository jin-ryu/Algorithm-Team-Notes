from collections import deque
# 시간 초과 나왔었음 - 정답 코드 참고함
# 이미 상하좌우로 탐색을 한 바이러스는 더 탐색을 안해도 됨
# 따라서 큐에서 pop해서 다음 탐색에서는 제거하는 방식으로 구현

n, k = map(int, input().split())
board = []
virus = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] != 0:
            virus.append((board[i][j], i, j, 0))  # 바이러스 종류, 위치 저장, 시간

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 적용
virus.sort()    # 번호가 낮은 순으로 정렬
queue = deque(virus)
while queue:
    v, x, y, s = queue.popleft()
    if s == target_s:   # target_s초가 지나면 종료
        break

    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:  # 아직 바이러스가 증식하지 않았다면
                board[nx][ny] = v   # 바이러스 증식
                queue.append((board[nx][ny], nx, ny, s+1))    

print(board[target_x-1][target_y-1])



