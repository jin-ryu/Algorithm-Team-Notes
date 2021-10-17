from collections import deque

def solution(board):
    answer = 0
    dic = {
        'E' : (0, -1),
        'W' : (0, 1),
        'S' : (1, 0),
        'N' : (-1, 0) 
    }
    corner = 0
    q = deque([(0, 0, '', 0, 0)])
    visited = []
    
    while q:
        x, y, d, l, c = q.popleft()
        print(x, y, d, l, c)
        if x == len(board)-1 and y == len(board[0])-1:
            print("finished")
            #break
        
        for D in dic.keys():
            dx, dy = dic[D]
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                if board[nx][ny] == 0: #(nx, ny) not in visited:
                    #visited.append((nx, ny))
                    if d != '' and d != D:
                        q.append((nx, ny, D, l+1, c+1))
                    else:
                        q.append((nx, ny, D, l+1, c))
    
    
    return answer