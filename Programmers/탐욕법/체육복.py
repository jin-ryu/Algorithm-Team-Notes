# 인터넷 참고
def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)

    answer = n - len(set_lost)

    return answer

n = 5
lost = [2,4]
reserve = [1,3,5]
print(solution(n, lost, reserve))

n1 = 5
lost1 = [2,4]
reserve1 = [3]
print(solution(n1, lost1, reserve1))

n2 = 3
lost2 = [3]
reserve2 = [1]
print(solution(n2, lost2, reserve2))