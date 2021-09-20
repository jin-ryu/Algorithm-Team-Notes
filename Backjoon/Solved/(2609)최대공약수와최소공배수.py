import math

n, m = map(int, input().split())
print(math.gcd(n, m))
print((n*m) // math.gcd(n,m))


# 직접 구현
def get_primes(n):
    primes = []
    for i in range(1, n+1):
        if n%i == 0:
            primes.append(i)

    return primes

def gcd(a, b):
    # 최대공약수
    cd = set(get_primes(a)) & set(get_primes(b))
    cd = sorted(list(cd))

    return cd[-1]

def lcm(a, b):
    # 최소공배수(= a*b // 최대공약수)
    return (a*b) // gcd(a,b)

n, m = map(int, input().split())
print(gcd(n, m))
print(lcm(n, m))