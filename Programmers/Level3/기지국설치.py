def solution(n, stations, w):
    answer = 0
    arr = []
    
    for s in stations:
        l, r = 0, 0
        if s-w >= 1:
            l = s-w
        else:
            l = 0
        
        if s+w <= n:
            r = s+w
        else:
            r = n+1
            
        arr.append((l, r))
    
    arr.append((n+1, n+1))
    
    now = 1
    size = 2*w+1
    for l, r in arr:
        if now < l:
            cnt = (l-now) // size   # 전파가 전달되지 않는 구간 개수
            if (l-now) % size != 0:
                cnt += 1
            answer += cnt   # 놓을 수 있는 기지국 최소값 계산
        
        now = r+1   # 다음 구간으로 이동
    
    return answer