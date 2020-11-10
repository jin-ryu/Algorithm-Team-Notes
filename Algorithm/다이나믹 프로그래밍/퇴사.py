import copy

n = int(input())
data = [()]  
for _ in range(1, n+1):
    data.append(tuple(map(int, input().split())))

days = {}
for i in range(1, n+1):
    for j in range(1, i):
        day =  i + data[i][0]   # i일에서 Ti만큼 후 날짜를 찾음
        if day > n: # 범위를 벗어나는 경우 생략
            continue
        # 해당 날짜에 도달할 수 있는 이전 날짜들을 리스트로 담음
        if day not in days.keys():
            days[day] = [i] 
        elif i not in days[day]:
            days[day].append(i)

print(days)

# DP 테이블 초기화/ i번째 날에 벌 수 있는 최대 금액
dp = [data[i][1] for i in range(n)]
for i in range(1, n+1):
    if i in days.keys():
        pass