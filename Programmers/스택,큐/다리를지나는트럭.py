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
class Bridge(object):
    def __init__(self, length, weight):
        self.max_length = length        # 다리 길이보다 더 많은 트럭이 올라갈 수 없음
        self.max_weight = weight
        self.queue = deque()
        self.current_weight = 0

    def push(self, truck):
        next_weight =  self.current_weight + truck
        if next_weight <= self.max_weight and len(self.queue) < self.max_length:
            self.queue.append(truck)
            self.current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self.queue.popleft()
        self.current_weight -= item
        return item

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return "Bridge({}/{} : [{}]".format(self.current_weight, self.max_weight, list(self.queue))

   
    

bridge_length1 = 2
weight1 = 10
truck_weights1 = [7,4,5,6]
print(solution(bridge_length1, weight1, truck_weights1))

bridge_length2 = 100
weight2 = 100
truck_weights2 = [10]
print(solution(bridge_length2, weight2, truck_weights2))


bridge_length3 = 100
weight3 = 100
truck_weights3 = [10,10,10,10,10,10,10,10,10,10]