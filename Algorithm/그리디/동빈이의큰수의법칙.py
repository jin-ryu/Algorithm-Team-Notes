def solution(N, M, K, data):
    result = 0

    data.sort()
    max_nums = [data[-1]] * K + [data[-2]] # 제일 큰 수 K개, 두번째로 큰수 1개 패턴을 반복함
    
    for i in range(M):
        result += max_nums[i%len(max_nums)]
    
    return result


# 정답 코드 : 시간복잡도가 더 좋음
def answer():
    # N, M, K를 공백을 기준으로 구분하여 입력 받기
    n, m, k = map(int, input().split())
    # N개의 수를 공백을 기준으로 구분하여 입력 받기
    data = list(map(int, input().split()))

    data.sort() # 입력 받은 수들 정렬하기
    first = data[n - 1] # 가장 큰 수
    second = data[n - 2] # 두 번째로 큰 수

    # 가장 큰 수가 더해지는 횟수 계산
    # k+1개: first*k + second
    count = int(m / (k + 1)) * k    # 완전한 묶음으로 셀 수 있는 거 계산
    count += m % (k + 1)        # 묶음에 포함되지 않는 나머지 계산

    result = 0
    result += (count) * first # 가장 큰 수 더하기
    result += (m - count) * second # 두 번째로 큰 수 더하기

    print(result) # 최종 답안 출력


print(solution(5, 8, 3, [2, 4, 5, 4, 6]))
print(solution(5, 7, 2, [3, 4, 3, 4, 3]))
#answer()
