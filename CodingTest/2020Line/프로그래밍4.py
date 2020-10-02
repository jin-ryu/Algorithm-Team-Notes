UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3   

def solution(maze):
    y, x = 0, 0
    time = 0
    return dfs(y, x, maze, time, RIGHT)

def dfs(y, x, maze, time, dir):
    if y == len(maze)-1 and x == len(maze)-1:   # 도착지 도달하면 time return
        return time

    # 상하좌우 방향으로 탐색
    if dir == RIGHT:
        new_dir = UP
        left_y, left_x = y-1, x
        right_dir = DOWN    # 다음 방향을 탐색하기 위해 
    elif dir == DOWN:
        new_dir = RIGHT
        left_y, left_x = y, x+1
        right_dir = LEFT    
    elif dir == LEFT:
        new_dir = DOWN
        left_y, left_x = y+1, x
        right_dir = UP
    else:
        new_dir = LEFT
        left_y, left_x = y, x-1
        right_dir = RIGHT


    # 더 이상 움직일 수 없는 경우
    if left_y < 0 or left_y >= len(maze) or left_x < 0 or left_x >= len(maze) or maze[left_y][left_x] == 1:
        return dfs(y, x, maze, time, right_dir) 
    else:
        return dfs(left_y, left_x, maze, time+1, new_dir)


print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))
"""
print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]))
print(solution([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]))
"""