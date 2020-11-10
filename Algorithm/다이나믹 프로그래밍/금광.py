def solution(test_case, n, m):
    for j in range(1, m):
        for i in range(0, n):
            max_value = 0
            if i - 1 >= 0 :  # 왼쪽 위에서 온 것
                max_value = max(max_value, test_case[i-1][j-1])
            if i + 1 < n:   # 왼쪽 아래서 온 것
                max_value = max(max_value, test_case[i+1][j-1])
            max_value = max(max_value, test_case[i][j-1])   # 왼쪽에서 온 것
            test_case[i][j] += max_value

    return max(list(zip(*test_case))[-1])

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    test = list(map(int, input().split()))
    test_case = []

    # m x n matrix로 만들기
    start, end = 0, m
    for _ in range(n):
        test_case.append(test[start:end])
        start = end 
        end = end + m

    print(solution(test_case, n, m))