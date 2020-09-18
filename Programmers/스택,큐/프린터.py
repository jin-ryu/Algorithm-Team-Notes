from collections import deque

def solution(priorities, location):
    queue = deque()
    done = deque()

    # 인덱스랑 우선순위 같이 보관
    for i, p in enumerate(priorities):
        queue.append((p, i))

    # 우선순위 순으로 done 큐에 추가
    while queue:
        max_priority = max(queue)[0]
        q = queue.popleft()
        if q[0] < max_priority:
            queue.append(q)
        else:
            done.append(q)
    
    # location의 실행순서 계산
    answer = 0
    while True:
        answer += 1
        q = done.popleft()
        if q[1] == location:
            break
    return answer



priorities1 = [2, 1, 3, 2]
location1 = 2
print(solution(priorities1, location1))

priorities2 = [1, 1, 9, 1, 1, 1]
location2 = 0
print(solution(priorities2, location2))