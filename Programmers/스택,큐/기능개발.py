from collections import deque

# 내가 푼 방법
def solution(progresses, speeds):
    answer = []
    dq_progresses = deque(p for p in progresses)
    dq_speeds = deque(s for s in speeds)

    count = 0
    while dq_progresses:
        # 일 진행
        for _ in range(len(dq_progresses)):
            p = dq_progresses.popleft()
            s = dq_speeds.popleft()
            if p <= 100:
                dq_progresses.append(p+s)
            else:   # 100이 넘어버린 일은 그대로 둠
                dq_progresses.append(p)
            dq_speeds.append(s)

        # 배포  
        for _ in range(len(dq_progresses)):
            p = dq_progresses.popleft()
            if p >= 100:
                dq_speeds.popleft()
                count += 1
            else:   # 앞에서 100을 넘은 일이 없다면 그냥 원상복구
                dq_progresses.appendleft(p)
                break
        
        # 카운트 추가
        if count != 0:
            answer.append(count)
            count = 0
        
    return answer


# 해결 방법 1 - zip 활용
def solution2(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):   
        # -((p-100)//s)
        # math.ceil 없이 올림하기 위해 사용
        # (p-100) 음수, (p-100)//s 내림한 음수(음수에서 내림은 절대값 커짐)
        # -((p-100)//s) 올림한 양수 
        if len(Q)==0 or Q[-1][0] < -((p-100)//s): 
            Q.append([-((p-100)//s), 1])
            print(-((p-100)//s))
        else:
            Q[-1][1] += 1
        
        print(Q)

    return [q[1] for q in Q]

progresses = [93, 30, 55]
speeds =[1, 30, 5]
print(solution(progresses, speeds))
print(solution2(progresses, speeds))