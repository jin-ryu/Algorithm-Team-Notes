def roll(dice, d):
    if d == 1:      # 동쪽
        bottom =  dice[3][0]
        right = dice[1][2]

        dice[3] = [right]
        dice[1] = [bottom] + dice[1][:2]
        
    elif d == 2:    # 서쪽
        bottom =  dice[3][0]
        left = dice[1][0]
        
        dice[3] = [left]
        dice[1] = dice[1][1:] + [bottom]

    elif d == 3:    # 북쪽
        arr = []
        for i in range(len(dice)):
            if i == 1:
                arr.append(dice[1][1])
            else:
                arr.append(dice[i][0])
        
        arr = arr[1:] + [arr[0]]

        for i in range(len(dice)):
            if i == 1:
                dice[1][1] = arr[i]
            else:
                dice[i][0] = arr[i]
        
    elif d == 4:     # 남쪽
        arr = []
        for i in range(len(dice)):
            if i == 1:
                arr.append(dice[1][1])
            else:
                arr.append(dice[i][0])
        
        arr = [arr[3]] + arr[:3]

        for i in range(len(dice)):
            if i == 1:
                dice[1][1] = arr[i]
            else:
                dice[i][0] = arr[i]

    return dice

N, M, x, y, K= map(int, input().split())
Map =[list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

dice = [
    [0],
    [0, 0, 0],
    [0],
    [0]
    ]

for d in orders:
    dx, dy = x, y
    if d == 1:      # 동쪽
        dy += 1     
    elif d == 2:    # 서쪽
        dy -= 1 
    elif d == 3:    # 북쪽
        dx -= 1
    elif d == 4:     # 남쪽
        dx += 1

    if 0 <= dx < N and 0 <= dy < M:
        x, y = dx, dy           # 지도 좌표 갱신
        dice = roll(dice, d)    # 주사위 굴리기

        if Map[x][y] == 0:
            # 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
            Map[x][y] = dice[3][0] 
        else:
            # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
            dice[3][0] = Map[x][y]
            Map[x][y] = 0

        #print(dice)
        print(dice[1][1])

    
