import sys

N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(N)]

# binary search
houses.sort()

result = 0
start, end = 1, houses[-1] - houses[0]  # start: 공유기 사이 거리 최소값, end: 공유기 사이 거리 최대값

while start <= end:
    mid = (start + end) // 2    # 공유기 사이 최대 거리 
    old = houses[0]  # 직전에 공유기 설치한 집
    count = 1   # 공유기 설치한 집의 수 (첫번째 집에 우선 설치했다 가정)

    for i in range(1, len(houses)):
        if houses[i]-old >= mid:
            # 최대 거리 이상의 간격을 가진 집이 있다면 공유기 설치
            count += 1
            old = houses[i]
    
    if count >= C:
        # C개 보다 많은 공유기를 설치할 수 있으면 최대 거리를 늘림
        start = mid + 1 
        result = mid
    else:
        # C개 보다 적은 공유기를 설치할 수 있다면 최대 거리를 줄임
        end = mid - 1

print(result)