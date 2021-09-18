n = int(input())
numbers = list(map(int, input().split()))
count = 0 

for num in numbers:
    # 1은 소수가 아니므로 제외
    if num < 2:
        continue

    for i in range(2, num):
        # 소수 판별
        if num%i == 0:
            break
    else:
        count += 1
    
print(count)