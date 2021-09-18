import math

n, m = map(int, input().split())
print(math.gcd(n, m))
print((n*m) // math.gcd(n,m))