import heapq

N = int(input())
P = list(map(int, input().split()))

heapq.heapify(P)

result = 0
i = len(P)
while P:
    # 가장 작은 값을 가장 앞의 인덱스에 두기
    v = heapq.heappop(P)
    result += i * v
    i -= 1

print(result)