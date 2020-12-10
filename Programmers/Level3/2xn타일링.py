import sys
sys.setrecursionlimit(60000)    # 재귀 호출 범위 증가

def solution(n):
    # 정답 패턴이 피보나치 수열입
    fibo = [1 for _ in range(n+1)]
    fibo[2] = 2

    for i in range(3, n+1):
        # 경우의 수가 많아질 수 있으므로 숫자 조정
        fibo[i] = (fibo[i-1] + fibo[i-2]) % 1000000007
    
    return fibo[n] 

def solution2(n):
    # 피보나치 수열 메모리 사용하지 않고 구하는 법
    a, b = 1, 1
    for i in range(n):
        # fibo[n] = n번 반복한 후 앞에 있는 값
        a, b = b, a+b
    return a % 1000000007

def solution3(n):
    mem = [-1 for i in range(60001)] # 메모이제이션

    def dp(n):
        if mem[n] != -1: return mem[n]
        if n == 0: return 1 # 공집합도 1로본다
        if n == 1: return 1
        mem[n] = (dp(n-1) + dp(n-2)) % 1000000007
        return mem[n]

    return dp(n)

print(solution(1000))