
import sys

# 2017년 상금 세팅
A = [0]
A += [5000000] * 1
A += [3000000] * 2
A += [2000000] * 3
A += [500000] * 4
A += [300000] * 5
A += [100000] * 6

# 2018년 상금 세팅
B = [0]
B += [5120000] * 1
B += [2560000] * 2
B += [1280000] * 4
B += [640000] * 8
B += [320000] * 16

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())

    cost = 0
    if a != 0 and len(A) > a:
        cost += A[a]
    if b != 0 and len(B) > b:
        cost += B[b]

    print(cost)
