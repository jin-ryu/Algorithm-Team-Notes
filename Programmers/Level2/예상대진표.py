def solution(n,a,b):
    answer = 0
    athletes = [i for i in range(1, n+1)]

    while athletes:
        winners = []
        # 라운드 증가
        answer += 1
        for i in range(0, n, 2):
            # a와 b가 만나는 경우
            if athletes[i] in (a, b) and athletes[i+1] in (a,b):
                return answer
            # a와 b는 무조건 승리
            elif athletes[i+1] in (a, b):
                winners.append(athletes[i+1])
            # 나머지는 번호가 낮은 쪽이 승리한다고 가정
            else:
                winners.append(athletes[i])

        # 이긴 사람들 대상으로 다시 토너먼트
        athletes = winners
        n = n//2

    return answer

# 좋은 풀이
def solution2(n, a, b):
    answer = 0
    while a != b:
        answer += 1
        # (숫자+1)//2: 다음 라운드에서의 인덱스
        a, b = (a+1)//2, (b+1)//2

print(solution(8, 4, 7))    # 3