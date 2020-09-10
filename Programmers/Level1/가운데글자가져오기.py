def solution(s):
    N = len(s)
    if N%2 == 0:        # 짝수
        return s[N//2-1:N//2+1]
    return s[N//2]    # 홀수

s = "abcde"
print(solution(s))

s1 = "qwer"
print(solution(s1))