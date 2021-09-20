A, B  = map(int, input().split())

def make_arr(n):
    arr = []
    num = 1

    while len(arr) < n:
        if len(arr) + num < n:
            arr += [num for i in range(num)]
        else:
            arr += [num for i in range(n - len(arr))]
        num += 1

    return arr

arr = make_arr(B)
prefix_sum = [0]
sum = 0

for i in range(B):
    sum += arr[i]
    prefix_sum.append(sum)

print(prefix_sum[B] - prefix_sum[A-1])
