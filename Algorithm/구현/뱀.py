from collections import deque

N = int(input())         # 보드의 크기
K = int(input())    # 사과의 개수

apples = [] # 사과 좌표
for _ in range(K):
    x, y = map(int, input().split())
    apples.append((x-1, y-1))

changes = []    # 방향 변환 
L = int(input())    # 방향 변환 횟수
for _ in range(L):
    time, direction = input().split()
    changes.append((int(time), direction))


RIGHT, LEFT, DOWN, UP = (0,1), (0,-1), (1,0), (-1,0)
arrow = RIGHT   # 현재 방향
snake = deque([(0,0)])   # 뱀이 위치한 좌표   
current = (0, 0)  # 현재 뱀의 위치
k = 0   # changes의 인덱스
time = 0    

while 0 <= current[0] < N and 0 <= current[1] < N:    # 벽의 범위 안에 있는 동아
    current = (current[0]+arrow[0], current[1]+arrow[1])   # 방향 따라서 이동
    time += 1
    if current in snake:    # 자신의 몸과 충돌했으므로 종료
        break
    else:
        snake.append(current)   # 뱀 몸길이 증가

    # 사과 있는지 확인
    for a in range(len(apples)):
        if apples[a] == current:
            del apples[a]
            break
    else:
        snake.popleft() # 꼬리 칸을 비워줌
    
    if k >= len(changes):
        continue
    # 방향 전환
    elif changes[k][0] == time:  
        if changes[k][1] == 'L':
            if arrow == RIGHT:
                arrow = UP
            elif arrow == UP:
                arrow = LEFT
            elif arrow == LEFT:
                arrow = DOWN
            elif arrow == DOWN:
                arrow = RIGHT

        elif changes[k][1] == 'D':
            if arrow == RIGHT:
                arrow = DOWN
            elif arrow == DOWN:
                arrow = LEFT
            elif arrow == LEFT:
                arrow = UP
            elif arrow == UP:
                arrow = RIGHT

        k += 1
    
print(time)



