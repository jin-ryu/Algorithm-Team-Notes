def rotate(D, d):
    if D == 'L':
        if d == 'E':
            return 'N'
        elif d == 'W':
            return 'S'
        elif d == 'S':
            return 'E'
        elif d == 'N':
            return 'W'
        
    elif D == 'R':
        if d == 'E':
            return 'S'
        elif d == 'W':
            return 'N'
        elif d == 'S':
            return 'W'
        elif d == 'N':
            return 'E'
    
    else:
        return d
        
        
def move(grid, now, d):
    x, y = now
    dx, dy = direction[d]
    
    # 현재 방향으로 이동
    nx = (x + dx + len(grid)) % len(grid)
    ny = (y + dy + len(grid[0])) % len(grid[0])
    
    # 이동 방향 변경
    d = rotate(grid[nx][ny], d)

    return (nx, ny), d
        
def solution(grid):
    answer = []
    visited = []
    global direction
    direction = {
        'E' : (0, 1),
        'W' : (0, -1),
        'S' : (1, 0),
        'N' : (-1, 0)
    }
    
    for k in direction.keys():
        if k in visited:
            continue
            
        now = (0,0)
        v = set([])
        c = 0
        d = k
        
        while True:
            now, d = move(grid, now, d)
            c += 1
            v.add((now, d))
            
            if now == (0,0) and direction[d] == direction[k]:
                break
        
        if v not in visited:
            answer.append(c)
            visited.append(v)
        
    answer.sort()
    return answer