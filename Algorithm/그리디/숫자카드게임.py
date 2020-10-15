# N개의 각 행에서 가장 작은 원소들 사이에서 가장 큰 원소의 값은 무엇인가?
def solution(N, M, cards):
    result = 0
    new_cards = []
    start = 0

    for _ in range(N):
        new_cards.append(cards[start:start+M])
        start += M
    
    for i in range(N):
        result = max(result, min(new_cards[i]))

    return result

# 정답 코드
def answer():
    # N, M을 공백을 기준으로 구분하여 입력 받기
    n, m = map(int, input().split())

    result = 0
    # 한 줄씩 입력 받아 확인하기
    for i in range(n):
        data = list(map(int, input().split()))
        # 현재 줄에서 '가장 작은 수' 찾기
        min_value = 10001
        for a in data:
            min_value = min(min_value, a)
        # '가장 작은 수'들 중에서 가장 큰 수 찾기
        result = max(result, min_value)

    print(result) # 최종 답안 출력
    

print(solution(3, 4, [1, 9, 3, 7, 6, 2, 11, 8, 5, 4, 10, 12]))
print(solution(3, 3, [10, 3, 5, 2, 4, 7, 6, 9, 1]))