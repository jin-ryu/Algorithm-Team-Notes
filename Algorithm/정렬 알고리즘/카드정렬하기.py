# 정답 코드 참고
import heapq

n = int(input())
sizes = []
for _ in range(n):
    sizes.append(int(input()))

result = 0
heapq.heapify(sizes)

# 가장 작은 카드 묶음 2개를 뽑아서 더해야 함
# 우선순위 큐를 이용하는 문제 (값이 작을수록 우선순위가 높음)
while len(sizes) > 1:
    group1 = heapq.heappop(sizes)
    group2 = heapq.heappop(sizes)
    # 합친 값을 다시 힙에 추가
    sum_value = group1 + group2
    result += sum_value
    heapq.heappush(sizes, sum_value)  

print(result)
