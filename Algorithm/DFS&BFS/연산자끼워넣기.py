from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))

ADD, SUBTRACT, MULTIPLE, DIVIDE = 0, 1, 2, 3
ops = []
# 연산 개수만큼 코드 집어 넣음
ops.extend([ADD]*add)
ops.extend([SUBTRACT]*sub)
ops.extend([MULTIPLE]*mul)
ops.extend([DIVIDE]*div)

# 전체 경우의 수 순열로 파악
# 중복되는 경우는 set으로 제외
perm = list(set(permutations(ops, n-1))) 
min_value = int(1e9)
max_value = -int(1e9)
    
for i in range(len(perm)):
    value = a[0]    # 값 초기화
    for j in range(n-1):    # n-1번 반복 
        if perm[i][j] == ADD:
            value += a[j+1]
        elif perm[i][j] == SUBTRACT:
            value -= a[j+1]
        elif perm[i][j] == MULTIPLE:
            value *= a[j+1]
        elif perm[i][j] == DIVIDE:
            value //= a[j+1]
                
    min_value = min(min_value, value)
    max_value = max(max_value, value)


print(max_value)
print(min_value)