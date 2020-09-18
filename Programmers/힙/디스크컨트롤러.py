import heapq

def solution(jobs):
    answer = 0
    
    N = len(jobs)
    count, time, end = 0, 0, -1   # 수행한 프로세스 개수, 현재 시간, 프로세스 종료 시점
    queue = []


    while count < N:
        for job in jobs:
            # 현재 시간 대기하고 있는 프로세스들을 힙에 추가
            if end < job[0] <= time:
                answer += time - job[0]    # 현재 시간까지 대기한 시간 추가
                heapq.heappush(queue, job[1])
        
        # 힙에 대기하는 프로세스가 있다면 가장 빨리 끝나는 프로세스 실행
        if len(queue) > 0:
            # 현재 실행중인 프로세스가 끝날 때까지 걸린 시간 추가 
            # 힙에 대기하는 프로세스가 2개 이상이면, 실행 중인 프로세스가 끝날 때까지 걸린 시간이 대기시간이 됨
            # 따라서 힙의 크기 * 현재 프로세스의 실행시간
            answer += len(queue) * queue[0] 
            end = time
            time += heapq.heappop(queue)
            count += 1
        # 큐에 대기하는 프로세스가 없다면 시간 +1
        else:
            time += 1

    return answer//N

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))