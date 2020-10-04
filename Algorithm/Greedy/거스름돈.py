def solution(N):
    charge = [500, 100, 50, 10]
    count = 0
    index = 0

    while N > 0:
        while N - charge[index] >= 0:   # 해당 거스름돈으로 거슬러 줄 수 있을 만큼 거슬러줌
            N -= charge[index]
            count += 1
        index += 1  # 거스름돈 변경

    return count

# 정답 코드
def answer(n):
    count = 0

    # 큰 단위의 화폐부터 차례대로 확인하기
    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        count += n // coin  # 해당 화페로 거슬러 줄 수 있는 동전의 개수 세기
        n %= coin

    return count


print(solution(1250), answer(1250))   # 5
print(solution(3000), answer(3000))   # 6
print(solution(10160), answer(10160))  # 23