# 시간초과 나기 쉬운 문제
# 남아 있는 연산자가 있다면 재귀적으로 연산 진행

N = int(input())
A = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
answer = []

def calculate(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    else:
        return int(a/b)

def backtracking(idx, result, answer):
    global A, a, b, c, d

    if idx >= len(A):
        answer.append(result)
        return

    if a > 0:
        a -= 1
        backtracking(idx+1, calculate(result, A[idx], '+'), answer)
        a += 1
    if b > 0:
        b -= 1
        backtracking(idx+1, calculate(result, A[idx], '-'), answer)
        b += 1
    if c > 0:
        c -= 1
        backtracking(idx+1, calculate(result, A[idx], '*'), answer)
        c += 1
    if d > 0:
        d -= 1
        backtracking(idx+1, calculate(result, A[idx], '/'), answer)
        d += 1

answer = []
backtracking(1, A[0], answer)
print(max(answer))
print(min(answer))