def check(result):
    # 현재 결과가 기준을 만족하는지 확인
    for r in result:
        x, y, a = r

        if a == 0:   # 기둥일 경우
            if not(y == 0 or [x, y-1, 0] in result or [x-1, y, 1] in result or [x, y, 1] in result):            
                break
        elif a == 1:   # 보일 경우
            if not([x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result)):
                break
    else:
        return True

    
    return False


def do(frame, result):
    x, y, a, b = frame

    if b == 1:   # 설치
        result.append([x, y, a])
        if not check(result):
            result.pop()
                
    else:   # 삭제
        idx = result.index([x, y, a])
        result.pop(idx)
            
        if not check(result):
            result.append([x, y, a])
        
def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        do(frame, answer)

    answer.sort()
        
    return answer