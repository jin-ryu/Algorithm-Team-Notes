n = int(input()) # 전체 팀의 수
last_year = list(map(int, input().split()))
m = int(input()) # 등수가 바뀐 팀수
changed = []
for _ in range(m):
    x, y = map(int, input().split())
    changed.append((x, y))

