from collections import deque
from sys import stdin
input = stdin.readline

# 입력
n, k = map(int, input().split())
a = deque(map(int, input().split()))

up, down = 0, n-1
robot = deque([0] * (n*2))     # 로봇의 위치

# 로봇 이동
def move():
    global start, a, robot, up, down, n

    # 가장 먼저 벨트에 올라간 로봇부터 이동
    for i in range(n-2, -1, -1):
        now, nxt = i, i+1

        if robot[now] == 1 and robot[nxt] == 0 and a[nxt] >= 1:
             # 로봇이 있고, 이동이 가능하면 이동
            robot[now] = 0
            robot[nxt] = 1
            a[nxt] -= 1     # 이동한 칸의 내구도 감소

    robot[down] = 0     # 내리는 위치에 있는 로봇은 내림
        


# 로봇 올림
def goUp():
    if robot[up] == 0 and a[up] != 0:
        # 로봇이 없고, 올릴 수 있다면 올림
        a[up] -= 1  # 올린 칸의 내구도 감소
        robot[up] = 1


level = 0
while a.count(0) < k:
    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
    level += 1

    # 1: 회전
    a.rotate(1)
    robot.rotate(1)
    robot[down] = 0     # 내리는 위치에 있는 로봇은 내림
 
    # 2: 이동
    move()

    # 3: 올림
    goUp()

print(level)




