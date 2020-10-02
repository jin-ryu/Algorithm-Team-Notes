def getPrice(cancel):
    if cancel == 0:
        return 100
    elif cancel == 1:
        return 50
    elif cancel == 2:
        return 25

    return 0

def solution(n, p, c):
    cancel_count = 0    # 취소 횟수
    left = 0        # 남은 탁구공
    total = 0       # 전체 수익
    price = 100       # 탁구공 가격

    for i in range(n):
        left += p[i]    # 탁구공 생산
        
        if left - c[i] >= 0:     # 거래 가능
            total += getPrice(cancel_count)*c[i]
            left -= c[i]
            cancel_count = 0
        else:   # 거래 취소
            cancel_count += 1

        if cancel_count >= 3:   # 거래 종료
            break

    avg =  total/(i+1)

    return '%.2f' %avg  # 소수점 아래 둘째자리까지 문자로 표현

print(solution(6, [5, 4, 7, 2, 0, 6], [4, 6, 4, 9, 2, 3]))
print(solution(7, [6, 2, 1, 0, 2, 4, 3], [3, 6, 6, 2, 3, 7, 6]))