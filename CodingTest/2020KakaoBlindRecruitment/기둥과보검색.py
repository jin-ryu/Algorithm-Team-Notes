def solution(n, build_frame):
    answer = []

    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        print(build_frame[i], answer)
        if a == 0:  # 기둥
            if b == 1 and isAvailableColumn(x, y, answer):  # 설치
                answer.append([x, y, 0])
            else:
                answer.remove([x, y, 0])

                
            
        else:   # 보
            if b == 1 and isAvailableCloth(x, y, answer):  # 설치
                answer.append([x, y, 1])
            else:
                answer.remove([x, y, 1])
    

    answer.sort(key=lambda x: (x[0], x[1], x[2]))   # 정렬

    return answer

def isAvailableColumn(x, y, answer):
    # 바닥 위에 있는 경우 / 보 위에 있는 경우 / 다른 기둥 위에 있는 경우
    if (y == 0) or ([x-1, y, 1] in answer) or ([x, y-1, 0] in answer): 
        return True
    return False

def isAvailableCloth(x, y, answer):
    # 한쪽 끝 부분이 기둥 위에 있는 경우 / 양쪽 끝 부분이 다른 보와 동시에 연결되어 있는 경우
    if ([x, y-1, 0] in answer or [x+1, y-1, 0]) or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
        return True
    return False


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]