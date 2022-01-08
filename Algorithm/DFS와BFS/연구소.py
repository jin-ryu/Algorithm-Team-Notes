from itertools import combinations
import copy

def dfs(board, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = []
    for i in range(4):  # 사방으로 이동한 결과를 넣음
        stack.append((x+dx[i], y+dy[i]))

    while stack:
        x, y = stack.pop()
        # 범위 벗어나는 경우 탐색 제외
        if x<0 or x>=n or y<0 or y>=m:
            continue
        # 벽이거나 이미 바이러스가 퍼진 곳은 탐색 제외
        if board[x][y] == 1 or  board[x][y] == 2:
            continue
        
        board[x][y] = 2     # 바이러스 퍼짐
        for i in range(4):  # 사방으로 이동한 결과로 반복
             stack.append((x+dx[i], y+dy[i]))

    return board


n, m = map(int, input().split())
board = []
max_count = 0

for _ in range(n):
    board.append(list(map(int, input().split())))  

# 빈칸의 위치를 파악
zero = []
for i in range(n):
    for j in range(m):
        if board[i][j] ==0:
            zero.append((i,j))

# 벽을 3개 세우는 조합을 생성
comb = list(combinations(zero, 3))
for i in range(len(comb)):
    walls = comb[i]
    new_board =  copy.deepcopy(board)   # 깊은 복사
    
    # 새로운 보드에 벽 채우기
    for j in range(len(walls)):
        x,y = walls[j]
        new_board[x][y] = 1

    # 바이러스 퍼진 결과 확인하기
    for x in range(n):
        for y in range(m):
            if board[x][y] == 2:    # 바이러스가 있다면 사방으로 퍼트림
                new_board = dfs(new_board, x, y)

    # 안전 영역 크기 계산
    count = 0
    for i in range(n):
        for j in range(m):
            if new_board[i][j] == 0:
                count += 1
    if count > max_count:
        max_count = count

print(max_count)