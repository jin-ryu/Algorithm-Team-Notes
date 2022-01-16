N, K = map(int, input().split())

time = [0] * (K+1)
cnt = [1] * (K+1)

t = 0
for i in range(N, -1, -1):
    time[i] = t
    t += 1

t = 0
for i in range(N, K+1):
    time[i] = t
    t += 1

for i in range(0, K+1, 2):
    # 이전 최단 시간에서 순간 이동 한 시간과 비교
    time[i] = min(time[i], time[i//2]+1)   

for i in range(K+1):
    # 이전 최단 시간과 비교
    if i > 0:
        time[i] = min(time[i], time[i-1]+1)
    if i < K:
        time[i] = min(time[i], time[i+1]+1)

print(time)
print(time[K])


'''못풀음'''