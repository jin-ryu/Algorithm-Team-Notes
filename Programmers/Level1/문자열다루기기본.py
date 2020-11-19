import string
def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    
    for ch in s:
        if ch not in string.digits:
            return False
    return True

# 좋은 풀이
def solution2(s):
    # s.isalpha(): 문자열이 문자인지 아닌지 True, False로 리턴
    # s.isdigit(): 문자열이 숫자인지 아닌지 True, False로 리턴
    return s.isdigit() and len(s) in (4, 6)

print(solution2("a234")) # false
print(solution2("1234")) # true