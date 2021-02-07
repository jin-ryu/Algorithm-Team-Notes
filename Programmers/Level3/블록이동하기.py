from collections import deque

def move(now1, now2, board):
    # 1초동안 now에서 움직일 수 있는 모든 경우를 반환
    result = set([])

    # 평행이동
    m = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dy, dx in m:
        nxt1 = (now1[0] + dy, now1[1] + dx)
        nxt2 = (now2[0] + dy, now2[1] + dx)
        if board[nxt1[0]][nxt1[1]] == 0 and board[nxt2[0]][nxt2[1]] == 0:
            # 이동시 벽이 아니라면 추가
            result.add((nxt1, nxt2))
            
    # 가로 회전
    if now1[0] == now2[0]:
        UP, DOWN = -1, 1
        for d in [UP, DOWN]:
            if board[now1[0] + d][now1[1]] == 0 and board[now2[0] + d][now2[1]] == 0:
                # 아래 or 위의 칸이 모두 빈칸인 경우만 회전 가능
                nxt1 = (now1[0] + d, now1[1])
                nxt2 = (now2[0] + d, now2[1])
                result.add((now1, nxt1))
                result.add((now2, nxt2))
                
    # 세로 회전
    else:
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if board[now1[0]][now1[1] + d] == 0 and board[now2[0]][now2[1] + d] == 0:
                # 왼쪽 or 오른쪽의 칸이 모두 빈칸인 경우만 회전 가능
                nxt1 = (now1[0], now1[1] + d)
                nxt2 = (now2[0], now2[1] + d) 
                result.add((nxt1, now1))
                result.add((nxt2, now2))
            
    return result
        

def bfs(n, board):
    # (n,n)까지의 최단 거리 탐색
    # 현재 좌표와 거리를 큐에 삽입
    queue = deque([((1, 1), (1, 2), 0)])
    # set안에 들어가는 것은 해시가 가능해야 한다 (리스트는 불가)
    visited = set([((1, 1), (1, 2))])
   
    while queue:
        now1, now2, dist = queue.popleft()
        for nxt in move(now1, now2, board):
            # 중복 좌표 제거하기 위해 정렬
            nxt = tuple(sorted([*nxt]))

            # 현재 좌표에서 1초동안 움직일 수 있는 모든 좌표를 탐색
            if (n, n) in nxt:
                # 하나라도 도착하면 종료
                return dist + 1

            if nxt not in visited:
                # 방문하지 않은 좌표를 방문
                visited.add((nxt))
                queue.append((*nxt, dist+1))
                
def solution(board):
    n = len(board)
    # 경계값 처리하기 위해 테두리에 벽을 세움
    new_board = [[1 for _ in range(n+2)] for _ in range(n+2)]
    
    for i in range(n):
        for j in range(n):
            # 원래 보드 값 채우기
            new_board[i+1][j+1] = board[i][j]
            
    return bfs(n, new_board)

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
