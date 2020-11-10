n, m = map(int, input().split())
value = [int(input()) for _ in range(n)]

# d[x]: x원을 만들기 위해 필요한 최소한의 화폐 개수
INF = int(1e9)
d = [INF] * (m+1)
# d 초기화
for v in value:
    if v <= m:  #\원하는 가격보다 작은 화폐만을 쓸 수 있음
        d[v] = 1

def dp():
    # 최소 화폐 단위보다 타겟 금액이 작은 경우
    if min(value) > m:
        return -1

    # 최소 화폐 단위부터 타겟 금액까지
    for i in range(min(value)+1, m+1):    
        for v in value:
            d[i] = min(d[i], d[i-v] + 1)    # v원을 사용한 것과 안한 것 중 적은 개수를 가짐

    if d[m] == INF:   # 만들 수 없는 경우
        return -1

    return d[m]        

print(dp())

