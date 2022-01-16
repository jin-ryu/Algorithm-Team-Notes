N = int(input())
M = int(input())

# union-find
root = [i for i in range(N+1)]
def find(x):
    if x == root[x]:
        return x
    
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        root[y] = x

# 길이 있으면 union
for i in range(N):
    arr = list(map(int, input().split())) 
    for j in range(N):
        if arr[j] == 1:
            union(i+1, j+1)

plan = list(map(int, input().split()))

for i in range(M-1):
    if find(plan[i]) != find(plan[i+1]):
        print("NO")
        break
else:
    print("YES")