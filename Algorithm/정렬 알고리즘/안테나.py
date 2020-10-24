n = int(input())
home = list(map(int, input().split()))

home.sort()

# 중간 지점을 찾음
mid = (home[0] + home[n-1]) // 2

# 중간 지점에서 거리가 가장 가까운 집을 선택
i = 0
nearest = []
while True:
    if mid-i in home:
        nearest.append(mid-i)
    if mid+i in home:
        nearest.append(mid+i)

    if nearest:     # 가장 가까운 집을 찾으면 종료
        break
    i += 1

nearest = list(set(nearest))
nearest.sort()
print(nearest[0])

