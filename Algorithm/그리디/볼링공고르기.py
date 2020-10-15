from collections import Counter
from itertools import combinations

def solution(N, M, weights):
    counter = dict(Counter(weights))
    counts = list(counter.values()) # 공 무게 종류별로 개수 카운트

    # 각 개수간의 곱의 합이 정답
    return sum(list(map(lambda x: x[0]*x[1], combinations(counts, 2))))

print(solution(5, 3, [1, 3, 2, 3, 2]))
print(solution(8, 5, [1, 5, 4, 3, 2, 4, 5, 2]))