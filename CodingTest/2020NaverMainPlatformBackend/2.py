import string
from itertools import permutations

def solution(S):
    # write your code in Python 3.6
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    N = len(S)

    # 부분 문자열 생성
    subs = []
    for i in range(N):
        for j in range(i+1, N+1):
            subs.append(S[i:j])

    balanced = []
    for sub in subs:
        for i in sub:
            if i in upper_letters:
                j = upper_letters.index(i)
                if lower_letters[j] not in sub:
                    break
            else:
                j = lower_letters.index(i)
                if upper_letters[j] not in sub:
                    break
        else:
            balanced.append(sub)

    if balanced:
        return min(list(map(len, balanced)))
    return -1
                   
    


print(solution("azABaabza"))
print(solution("TacoCat"))
print(solution("AcZCbaBz"))
print(solution("abcdefghijklmnopqrstuvwxyz"))