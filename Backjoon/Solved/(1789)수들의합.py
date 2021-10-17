S = int(input())

s = 0
n = 1
cnt = 0

while S-s >= n:
    # 지금까지 누적합이 다음 숫자보다 클 동안 반복
    s += n
    n += 1
    cnt += 1

print(cnt)