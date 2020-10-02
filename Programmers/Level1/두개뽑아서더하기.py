import itertools

def solution(numbers):
    combs = list(itertools.combinations(numbers, 2))
    answer = list(set([c[0]+c[1] for c in combs]))

    return sorted(answer)

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))