# 집을 정렬해서 최소 거리와 최대 거리를 계산하고 이들의 중간값을 계산
# 중간값을 기준으로 집의 개수를 셌을 때 C보다 크다면, 최소값을 중간값 + 1로 갱신하고,
# 중간값을 기준으로 집의 개수를 셌을 때 C보다 작다면, 최댓값을 중간값 - 1로 갱신한다.
# 이걸 계속 반복하는 데, 최솟값과 최댓값이 같아질 때까지 반복한다.

n, c = map(int, input().split())
array = list(map(int, input().split()))

array.sort()    # 이진 탐색 수행을 위해 정렬

start = array[1] - array[0]    # 최소거리
end = array[-1] - array[0]     # 최대거리

while start < end:
    mid = (start + end) // 2    # mid는 가장 인접한 두 공유기 사이의 거리(Gap)을 의미
    # 첫번째 집에는 무조건 공유기를 설치한다고 가정
    value = array[0]
    count = 1

    # 현재의 mid 값을 이용해 공유기를 설치하기
    for i in range(1, n): # 앞에서부터 차근차근 설치 
        if array[i] >= value + mid:     # 현재 설치된 위치에서 mid 이상의 거리에 있는 집이면 설치
            value = array[i]
            count += 1
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가시키기
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소시키기
        end = mid - 1

print(result)