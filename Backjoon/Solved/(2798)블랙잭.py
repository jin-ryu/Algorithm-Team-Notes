from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

# 3개 숫자 합 정렬
comb = sorted(list(map(sum, combinations(card, 3))))
# m보다 작거나 같은 값만 필터링
comb = list(filter(lambda x: x <= m, comb))
# 결과 출력
print(comb[-1])
