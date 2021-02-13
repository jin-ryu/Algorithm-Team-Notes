n = int(input())
numbers = []
for i in range(n):
    x, y = map(int, input().split())
    numbers.append((x, y))

numbers.sort()

for i in range(n):
    print(numbers[i][0], numbers[i][1])