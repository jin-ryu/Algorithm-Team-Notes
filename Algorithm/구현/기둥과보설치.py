# 답안 코드 활용
# 어떤 조건이 맞을 때만 수행
# 1. 그 조건이 맞는지 판별하는 함수 생성
# 2. 일단 수행하고, 조건이 맞지 않는다면 되돌리기
def is_possible(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥
            if y==0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            return False

        elif a == 1:    # 보
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
        
    return True
               
def solution(n, build_frame):
    answer = []
    
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i] # 리스트도 언패킹 가능
        
        if b == 0: # 삭제
            answer.remove([x,y,a])
            if not is_possible(answer): # 삭제했을 때 조건에 안맞을 경우 되돌리기
                answer.append([x,y,a])  
                
        elif b == 1:    # 설치
            answer.append([x,y,a])      
            if not is_possible(answer): # 설치했을 때 조건에 안맞을 경우 되돌리기
                answer.remove([x,y,a])
        
    return sorted(answer)

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))