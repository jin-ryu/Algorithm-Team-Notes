N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

left = {
    0 : 3,
    1 : 0,
    2 : 1,
    3 : 2
}
dir = {
    0 : (-1, 0),
    1 : (0, 1),
    2 : (1, 0),
    3 : (0, -1)
}

isLoop = True
now = (r, c)
visited = [now]     # 현재 위치를 청소
cnt = 0

while isLoop:
    # 현재 방향 기준 왼쪽 좌표 생성
    dx = now[0] + dir[left[d]][0]
    dy = now[1] + dir[left[d]][1]

    if 0 <= dx < len(board) and 0 <= dy < len(board[0]):
        if board[dx][dy] == 0 and (dx, dy) not in visited:
            d = left[d]
            now = (dx, dy)
            cnt = 0     # 회전 횟수 초기화
            visited.append((dx, dy))
        elif cnt >= 4:
            # 네 방향 모두 청소가 이미 되어 있거나 벽인 경우
            ddx = now[0] - dir[d][0]
            ddy = now[1] - dir[d][1]
            if 0 <= ddx < len(board) and 0 <= ddy < len(board[0]):
                if board[ddx][ddy] == 0:
                    now = (ddx, ddy)
                    cnt = 0
                else:
                    isLoop = False
        else:
            d = left[d]
            cnt += 1

#print(visited)
print(len(visited))
