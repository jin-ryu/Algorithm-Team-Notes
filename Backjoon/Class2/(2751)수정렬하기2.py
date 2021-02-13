import sys

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
numbers.sort()

# 출력
for i in range(n):
    print(numbers[i])