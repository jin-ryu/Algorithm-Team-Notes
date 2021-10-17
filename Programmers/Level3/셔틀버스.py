def solution(n, t, m, timetable):
    answer = ''
    hour, minute = 9, 0
    arr = []    # 매 타임마다 타는 승객
    
    timetable.sort(key=lambda x: list(map(int, x.split(':'))), reverse=True)
    for i in range(n):
        temp = []
        while timetable:
            th, tm = timetable[-1].split(':')
            th, tm = int(th), int(tm)
            
            if th > hour or (th == hour and tm > minute) or len(temp) >= m:
                break
                
            temp.append(timetable.pop())
        
        arr.append(temp)
        
        if i != n-1:
            # 다음 셔틀버스 시간으로 이동
            minute += t
            if minute >= 60:
                hour += 1
                minute -= 60
    
    print(arr) 
    if m - len(arr[-1]) >= 1:
        # 마지막 시간에 남는 자리가 있는 경우
        answer = str(hour).zfill(2) + ":" + str(minute).zfill(2)
    else:
        # 남는 자리가 없는 경우
        th, tm = arr[-1][-1].split(":")
        th, tm = int(th), int(tm)    
        
        tm -= 1 # 가장 마지막에 타는 사람 빼기 1분
        if tm < 0:
            tm += 60
            th -= 1
                
        answer = str(th).zfill(2) + ":" + str(tm).zfill(2)
        
    return answer