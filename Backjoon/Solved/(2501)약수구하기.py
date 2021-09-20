N, K = map(int, input().split())

primes = []
for i in range(1, N+1):
    if N%i == 0:
        primes.append(i)
    
#print(primes)
if len(primes) > K-1:
    print(primes[K-1])
else:
    print(0)