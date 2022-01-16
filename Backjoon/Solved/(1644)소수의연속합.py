N = int(input())

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n+1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i] == True]

primes = prime_list(N)

# 누적 합 구하기
_sums = [0]
s = 0
for p in primes:
    s += p
    _sums.append(s)

# 투포인터로 연속되는 합이 있는지 확인
result = 0
l, r = 0, 1

while l <= r and r < len(_sums):
    v = _sums[r] - _sums[l]
    if v > N:
        l += 1
    else:
        r += 1
        if v == N:
            result += 1


print(result)
