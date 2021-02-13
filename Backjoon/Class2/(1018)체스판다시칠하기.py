n, m = map(int, input().split())
board = [input() for _ in range(n)]

white = "WBWBWBWB"
black = "BWBWBWBW"

def check(i, j, now):
    # 해당 박스의 다시 칠해야 하는 정사각형 최솟값을 반환
    global board
    global white, black
    count = 0

    for x in range(8):
        for y in range(8):
            # 바꿔야할 개수 카운트
            if board[x+i][y+j] != now[y]:
                count += 1

        # 줄 바꾸면 white, black 변경
        if now == white:
            now = black
        else:
            now = white
    
    return count
         

min_value = 2500   
for i in range(n-8+1):
    for j in range(m-8+1):
        # 보드 탐색
        min_value = min(min_value, check(i, j, black))
        min_value = min(min_value, check(i, j, white))


print(min_value)

