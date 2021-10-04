from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    lengths = [[-1 for j in range(m)] for i in range(n)]  # (x,y) 까지 가는 최단 경로 저장
    queue = deque([(0, 0)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]
    
    lengths[0][0] = 1
    
    # bfs 활용
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            _dx = x + dx[i]
            _dy = y + dy[i]
            
            if 0 <= _dx < n and 0 <= _dy < m and maps[_dx][_dy] == 1:
                if lengths[_dx][_dy] == -1:
                    lengths[_dx][_dy] = lengths[x][y] + 1
                    queue.append((_dx, _dy))    # 인접한 방문하지 않은 곳 큐에 추가
                
    return lengths[-1][-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))