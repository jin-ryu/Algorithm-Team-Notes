n, k  = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for _ in range(k):
    if min(A) < max(B):  # min(A) >= max(B) 이면 종료
        i = A.index(min(A))
        j = B.index(max(B))

        A[i], B[j] = B[j], A[i]
    else:
        break

print(sum(A))