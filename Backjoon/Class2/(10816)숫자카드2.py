from collections import Counter
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

m = int(input())
pivots = list(map(int, sys.stdin.readline().split()))

counter = dict(Counter(numbers))
for i in range(m):
    if pivots[i] not in counter.keys():
        print(0, end = " ")
    else:
        print(counter[pivots[i]], end=" ")
