n = int(input())
numbers = list(map(int, input().split()))
count = 0 

for num in numbers:
    # 1은 소수가 아니므로 제외
    if num < 2:
        continue

    for i in range(2, num):
        # 소수 판별
        if num%i == 0:
            break
    else:
        count += 1
    
print(count)


# 아리스토테네스의 체
def get_primes(n):
    isPrimes = [True for i in range(n+1)]
    if n > 1:
        isPrimes[1] = False
    
    for i in range(2, int(n*(1/2))+1):
        if isPrimes[i]:
            # 소수라면 소수의 배수들은 모두 소수가 아닌 것으로 처리
            j = 2
            while i*j < n+1:
                isPrimes[i*j] = False
                j += 1

    return isPrimes

n = int(input())
numbers = list(map(int, input().split()))

count = 0
isPrimes = get_primes(max(numbers))
for num in numbers: 
    if isPrimes[num]:
        count += 1

print(count)