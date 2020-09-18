import heapq

def solution(scoville, K):
    answer = 0
    heap =[]

    for s in scoville:
        heapq.heappush(heap, s)

    while heap:
        # 스코빌 지수로 만들수 없는 경우
        if len(heap) == 1 and sum(heap) < K:    
            return -1
        h1 = heapq.heappop(heap)
        if h1 >= K:     # 최소 값이 K 이상이면 작업 종료
            break
        h2 = heapq.heappop(heap)

        heapq.heappush(heap, h1+h2*2)
        answer += 1
    
    if answer == 0:
        return -1

    return answer

scoville = [1,1,1]
K = 7
print(solution(scoville, K))
