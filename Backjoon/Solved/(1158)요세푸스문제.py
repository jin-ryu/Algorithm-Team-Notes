n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
result = []
length = n
index = 0

for i in range(n):
    # 원순열을 k 만큼 이동
    index += (k-1)
    index %= length
    # k번째 사람 뽑아서 제거
    r = arr[index]
    result.append(r)
    arr.remove(r)
    length -= 1

# 결과 출력
print("<", end="")
for i in range(len(result)):
    print("%d" %result[i],  end= "")
    if i != n-1:
        print(", ", end = "")
print(">", end = "")
