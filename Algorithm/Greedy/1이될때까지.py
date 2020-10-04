def solution(N, K):
    count = 0

    while N != 1:
        if N % K == 0:  # K로 나눌 수 있을 때마다 나눠줌
            N //= K
        else:
            N -= 1
        count += 1
    
    return count

# 정답 코드
def answer():
    # N, K공백을 기준으로 구분하여 입력 받기
    n, k = map(int, input().split())

    result = 0

    # 로그시간 복잡도로 빠르게 해결 가능
    while True:
        # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
        target = (n//k) * k     # 가장 N과 가까운 K배수를 찾음
        result += (n-target)    # 1씩 더할 수 만큼 더해줌 (한꺼번에)
        n = target  # n을 k로 나눠 떨어지는 수로 만들어줌

        # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break

        # K로 나누기
        result += 1
        n //= k

    # 마지막으로 남은 수에 대하여 1씩 빼기 
    result += (n-1) # n이 1보다 크다면 나머지 연산을 한꺼번에 더해줌
    print(result)


print(solution(25, 5))  # 2
print(solution(17, 4))  # 3
answer()