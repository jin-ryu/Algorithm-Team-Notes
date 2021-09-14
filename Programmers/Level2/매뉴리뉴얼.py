from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        # 가능한 후보 조합 리스트를 전부 뽑음
        candidates = []
        for o in orders:
            comb = list(map(lambda x: "".join(sorted(x)), combinations(o, c)))
            candidates.extend(comb)
            
        # 후보 조합 카운트
        counter = Counter(candidates).most_common()
        # 최다 개수 조합 추가
        answer.extend([menu for menu, cnt in counter if cnt > 1 and cnt == counter[0][1]])
    
    # 정렬
    answer.sort()
    
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))