from itertools import combinations

def solution(N, coin_types):
    combination = set()

    # 동전으로 만들 수 있는 값을 계산
    for r in range(1, len(coin_types)+1):
        combination.update(map(sum, combinations(coin_types, r)))

    coin = 0
    while True:
        coin += 1
        if coin not in combination:
            return coin

    return 0

def answer():
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    target = 1  # target 이하의 값은 모두 만들 수 있다 정의
    for x in data:
        # 만들 수 없는 금액을 찾았을 때 반복 종료
        if target < x:
            break
        target += x

    # 만들 수 없는 금액 출력
    print(target)

#print(solution(5, [3, 2, 1, 1, 9]))
#print(solution(3, [3, 5, 7]))
answer()