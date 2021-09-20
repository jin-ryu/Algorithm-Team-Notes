M = int(input())
N = int(input())

def get_primes(n):
    isPrimes = [True for i in range(n+1)]
    for i in range(2, n+1):
        if isPrimes[i]:
            j = 2
            while i*j < n+1:
                isPrimes[i*j] = False
                j += 1

    # 1과 0은 소수에서 제외
    isPrimes[0] = False
    if len(isPrimes) > 1:
        isPrimes[1] = False
    
    return isPrimes

result = []
sum_value = 0
isPrimes = get_primes(N)

for i in range(M, N+1):
    if isPrimes[i]:
        result.append(i)
        sum_value += i

if result:
    print(sum_value)
    print(result[0])
else:
    print(-1)

