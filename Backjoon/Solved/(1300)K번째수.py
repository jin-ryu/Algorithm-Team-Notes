N = int(input())
k = int(input())

# binary search
start, end = 1, k   # start: 결과 값으로 나올 수 있는 최소값, end: 결과 값으로 나올 수 있는 최대값
result = 0

while start <= end:
    mid = (start + end) // 2

    # mid 보다 작은 i*j 가 몇개 있는지 카운트
    count = 0
    for i in range(1, N+1):
        count += min(mid//i, N)

    if count >= k:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)