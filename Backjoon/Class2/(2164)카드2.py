from collections import deque

n = int(input())

# 역순으로 큐에 삽입
numbers = deque([i for i in range(1, n+1)])

while len(numbers) > 1:
    # 마지막 카드 한장이 남을 때 까지 반복
    # 맨 위의 카드 제거
    numbers.popleft()
    # 맨 위 카드 맨 뒤로 보냄
    numbers.append(numbers.popleft())
   
print(numbers[0])