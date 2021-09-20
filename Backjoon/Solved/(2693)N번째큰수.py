T = int(input())
t = [list(map(int, input().split())) for i in range(T)]

for i in range(T):
    print(sorted(t[i])[-3])