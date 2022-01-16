import sys

N = int(sys.stdin.readline())
lengths = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

price = 1000000000 
result = 0

for i in range(N-1):
    price = min(prices[i], price)   # 항상 현재 기준 가장 작은 값으로 이동
    result += lengths[i] * price
    
print(result)
