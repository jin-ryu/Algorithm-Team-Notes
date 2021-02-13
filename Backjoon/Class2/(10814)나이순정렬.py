import sys

n = int(sys.stdin.readline())
info = []

for _ in range(n):
    i = sys.stdin.readline().split()
    info.append((int(i[0]), i[1]))

# 나이, 가입한 순 정렬
info.sort(key=lambda x: x[0])
for i in range(n):
    print(info[i][0], info[i][1])
