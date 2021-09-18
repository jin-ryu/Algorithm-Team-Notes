from functools import reduce

n, k = map(int, input().split())
if k == 0 or n == k:
    print(1)
else:
    up = reduce(lambda x, y : x * y, [n-i for i in range(k)])
    down =  reduce(lambda x, y : x * y, [k-i for i in range(k)])
    print(up // down)