def move(cur, d):
    # 방향에 따라 이동한 좌표를 반환
    nxt = ()
    if d == "U":
        nxt = (cur[0] - 1, cur[1])
    elif d == "D":
        nxt = (cur[0] + 1, cur[1])
    elif d == "R":
        nxt = (cur[0], cur[1] + 1) 
    elif d == "L":
        nxt = (cur[0], cur[1] - 1)
        
    if -5 <= nxt[0] <= 5 and -5 <= nxt[1] <= 5:
        # 좌표평면 안에 있는 명령만 반환
        return nxt

def solution(dirs):
    visited = set([])
    cur = (0, 0)
    for d in dirs:
        nxt = move(cur, d)
        if nxt:
            # 좌표평면 안에 있는 명령인 경우 경로 추가
            route = tuple(sorted([cur, nxt]))
            visited.add(route)
            # 현재 위치 갱신
            cur = nxt
    
    return len(visited)