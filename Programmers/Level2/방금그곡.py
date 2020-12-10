def get_sheet(sheet):
    # 악보에서 #이 있는 것을 소문자로 바꿈
    sheet = sheet.replace("C#", "c")
    sheet = sheet.replace("D#", "d")
    sheet = sheet.replace("F#", "f")
    sheet = sheet.replace("G#", "g")
    sheet = sheet.replace("A#", "a")
    
    return sheet
    
def solution(m, musicinfos):
    answer = []
    # #이 있는 음을 다 변경
    m = get_sheet(m)
    
    for i in range(len(musicinfos)):
        info = musicinfos[i].split(",")
        start, end = info[0], info[1]
        title, sheet = info[2], get_sheet(info[3])
        
        # 들은 시간 계산
        start = list(map(int, start.split(":")))
        end = list(map(int, end.split(":")))
        time = (end[0]-start[0])*60+(end[1]-start[1])
        
        # 들은 시간만큼 멜로디 생성 (몫과 나머지 이용)
        a = time // len(sheet)
        b = time % len(sheet)
        melody = sheet * a + sheet[:b]
        
        # 멜로디 안에 m이 있다면 정답리스트에 추가
        if m in melody:
            # 시간, 제목 입력 순서, 제목
            answer.append((time, i, title))
            
    # 재생 시간 순으로 정렬
    answer.sort(key = lambda x:(-x[0], x[1]))
    if answer:
        return answer[0][2]
        
    return "(None)"
    
print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])) # HELLO