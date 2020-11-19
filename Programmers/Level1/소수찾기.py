# 이중 포문 사용으로 시간 초과
def solution(n):
    count = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            count += 1
    return count

# 에라토네스의 체 활용: 소수인 것의 배수 지우기
def solution2(n):
    # n개의 요소에 True로 설정(소수로 간주)
    sieve = [True] * (n+1)

    # n의 최대 약수가 sqrt(n)이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] :   # 소수인 경우 배수 지움
            for j in range(i+i, n+1, i):
                sieve[j] = False
    
    prime = [i for i in range(2, n+1) if sieve[i] == True]

    return len(prime)

# 좋은 풀이
def solution3(n):
    num = set(range(2, n+1))    # 일단 전부 소수라 가정

    # n의 최대 약수가 sqrt(n)이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m+1): # 원래 n+1까지 했는데 줄이면 좋을 듯
        if i in num:    # 소수이면 본인 이후의 배수를 전부 빼줌
            num -= set(range(2*i, n+1, i))
    return len(num)

print(solution3(10))    # 4
print(solution2(5))     # 3
    
