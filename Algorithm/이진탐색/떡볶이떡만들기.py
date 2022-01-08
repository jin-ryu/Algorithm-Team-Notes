# 파라메트릭 서치: 최적화 문제를 Yes or No의 결정 문제로 바꾸어 해결하는 기법

n, m = map(int, input().split())
lengths = list(map(int, input().split()))

start = 0
end = max(lengths)
result = []     # M만큼의 떡을 얻을 수 있는 길이들

# 이진 탐색
while start <= end:
    mid = (start + end) // 2    # 절단기 높이를 중단점으로 가정
    left = 0    # 잘린 떡의 길이 합
    
    for i in range(n):
        if lengths[i] > mid:
            left += lengths[i] -  mid

    if left == m:
        result.append(mid)
        start = mid + 1     # 더 큰 숫자가 있나 탐색
    elif left < m:
        end = mid - 1
    else:
        start = mid + 1

print(max(result))