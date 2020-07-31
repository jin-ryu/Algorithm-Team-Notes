from collections import deque

# 내가 푼 방법
def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossing = deque([])
    times = deque([])
    weights = 0

    truck_weights.reverse()

    while True:
        answer += 1

        # 트럭 이동하기
        for _ in range(len(times)):     # 언더바로 하면 변수명 안 정할 수 있음
            time = times.popleft() - 1
            if time <= 0:
                weights -= crossing.popleft()
            else:
                times.append(time)
        
    
        # 트럭 올리기
        index = len(truck_weights) - 1
        if truck_weights and weights + truck_weights[index] <= weight:
            crossing.append(truck_weights[index])
            times.append(bridge_length)
            weights += truck_weights.pop()

        if not times:
            break

    return answer

# 해결 방법1 


bridge_length1 = 2
weight1 = 10
truck_weights1 = [7,4,5,6]
#print(solution(bridge_length1, weight1, truck_weights1))

bridge_length2 = 100
weight2 = 100
truck_weights2 = [10]
print(solution(bridge_length2, weight2, truck_weights2))


bridge_length3 = 100
weight3 = 100
truck_weights3 = [10,10,10,10,10,10,10,10,10,10]