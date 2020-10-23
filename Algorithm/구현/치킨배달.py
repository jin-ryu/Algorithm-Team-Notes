from itertools import combinations  # combination 임포트하는 방법 외우기

def getDistance(store, home):    
    total = 0

    for i in range(len(home)):
        min_distance = (N-1)*2  # 최대 거리로 초기화

        for j in range(len(store)):
            distance = abs(home[i][0]-store[j][0]) + abs(home[i][1]-store[j][1])
            if distance < min_distance:
                min_distance = distance

        total += min_distance

    return total
        

N, M = map(int, input().split())
city = []

for _ in range(N):
    city.append(list(map(int, input().split())))

store = []
home = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i,j))
        elif city[i][j] == 2:
            store.append((i,j))


comb = list(combinations(store, M)) # combination 사용하면 원하는 객체로 강제 형변환 해야함
distances = []
for c in comb:
    distances.append(getDistance(c,home))

print(min(distances))
