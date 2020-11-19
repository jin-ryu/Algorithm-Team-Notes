def solution(x):
    num = sum(map(int, list(str(x))))
    # num = sum([int(i) for i in str(x)])
    if x%num == 0:
        return True
    return False

print(solution(10)) # true
print(solution(12)) # true
print(solution(11)) # false
print(solution(13)) # false