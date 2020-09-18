import heapq

def solution(operations):
    answer = []
    max_queue, min_queue = [], [] # 최대 힙, 최소 힙
    for operation in operations:
        op = operation.split(' ')
        # op[0]: 명령어, op[1]: 값 
        if op[0] == "I":
            value = int(op[1])
            heapq.heappush(min_queue, value)
            heapq.heappush(max_queue, (-value, value))  # (우선순위, 값)

        # 최솟값 삭제
        elif max_queue and op[0] == "D" and op[1] == "-1":   
            poped_value = heapq.heappop(min_queue)
            max_queue.remove((-poped_value, poped_value))

        # 최댓값 삭제
        elif max_queue and op[0] == "D" and op[1] == "1": 
            poped_value = heapq.heappop(max_queue)[1]     # (우선순위, 값) 중에서 값만 추출
            min_queue.remove(poped_value) 

    if max_queue:   # 힙이 비어있지 않다면
        max_value = heapq.heappop(max_queue)[1]
        min_value = heapq.heappop(min_queue)
        answer = [max_value, min_value]
    else:   # 힙이 비어 있다면
        answer = [0,0]


    return answer

op = ["I 16","D 1"]
print(solution(op))
op1 = ["I 7","I 5","I -5","D -1"]
print(solution(op1))