n = int(input())
restaurant = list(map(int, input().split()))

# DP 테이블 생성
# d[x]: x번째 창고를 털었을 때 얻을 수 있는 최대 값
d = [0] * n
# 처음 식랑 초기화
for i in range(n):
    d[i] = restaurant[i]

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + d[i])

print(max(d))