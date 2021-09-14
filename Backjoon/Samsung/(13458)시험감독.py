from sys import stdin
input = stdin.readline

# 입력
n = int(input())
A = list(map(int, input().split()))
b, c = map(int, input().split())

# 한 고사장에 필요한 감독관 최소수
def count(a):
    global b, c
    if a <= b:
        return 1

    # 총 감독관(필수) + 부감독관
    cnt = 1 + (a-b)//c
    if (a-b)%c > 0:
        cnt += 1
    return cnt

result = 0
for a in A:
    result += count(a)

print(result)