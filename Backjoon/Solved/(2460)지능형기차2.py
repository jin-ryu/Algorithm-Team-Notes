t = [list(map(int, input().split())) for i in range(10)]

max_num = 0
current = 0

for o, i in t:
    current += i
    current -= o
    if current > max_num:
        max_num = current

print(max_num)