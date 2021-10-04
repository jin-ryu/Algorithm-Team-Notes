from collections import deque

def solution(enter, leave):
    answer = []
    result = [set() for _ in range(len(enter))]
    now = []
    
    enter = deque(enter)
    leave = deque(leave)
    while enter and leave:
        # 입장할 수 있는 만큼 입장하기
        while leave and leave[0] not in now:
            now.append(enter.popleft())
          
        # 만나는 원소 저장
        for i in now:
            for j in now:
                if i != j:
                    result[i-1].add(j)
                    result[j-1].add(i)
                    
        # 퇴장할 수 있을 만큼 퇴장하기
        while leave and leave[0] in now:
            now.remove(leave.popleft())
            
    return [len(result[i]) for i in range(len(result))]