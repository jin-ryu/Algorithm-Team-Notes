from bisect import bisect_left, bisect_right

n, c = map(int, input().split())
home = []
for _ in range(n):
    home.append(int(input()))

home.sort()  # 위치순 정렬
wifi = []
end = max(home)
start = 0

def binary_search(array, start, end, count):
    if start > end or count == c:
        return None

    mid = (start + end) // 2
    left_index = bisect_left(home, mid)
    right_index = bisect_left(home, mid)

    if abs(home[left_index] - mid) < abs(home[right_index] - mid):
        if home[left_index] not in wifi:
            wifi.append(home[left_index])
        binary_search(array, start, left_index-1, count+1)
        binary_search(array, left_index+1, end, count+1)
    else:
        if home[right_index] not in wifi:
            wifi.append(home[right_index])
        binary_search(array, start, right_index-1, count+1)
        binary_search(array, right_index+1, end, count+1)
    

binary_search(home, start, end, 0)
min_value = 1e9
wifi.sort()

# 가장 인접한 두 공유기 사이의 거리 계산
for i in range(c-1):
    value = wifi[i+1] - wifi[i]
    min_value = min(min_value, value)

print(min_value)