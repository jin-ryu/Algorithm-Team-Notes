H, W = map(int, input().split())
arr = list(map(int, input().split()))

# 최대 높이 인덱스 구함
max_value = max(arr)
idx = arr.index(max_value)

total = 0
h = 0
for i in range(idx+1):
    # 왼쪽에서 인덱스까지 최대 높이 더하기
    h = max(h, arr[i])
    total += h
    
h = 0
for j in range(len(arr)-1, idx, -1):
    # 오른쪽에서 인덱스까지 최대 높이 더하기
    h = max(h, arr[j])
    total += h
    
result = total - sum(arr)
print(result)
    
    