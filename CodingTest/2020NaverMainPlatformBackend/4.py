def solution(A):
    def search(x, y, A, B, value):
        # x, y 범위 체크
        if x < 0 or x >= len(A):
            return
        if y < 0 or y >= len(A[0]):
            return

        if B[x][y] == 1:    # 이미 탐색한 것은 더 탐색하지 않음
            return

        if A[x][y] != value:    # 값이 다른 건 다른 나라
            return

        B[x][y] = 1        # 탐색했음 표시
        search(x+1, y, A, B, value)
        search(x-1, y, A, B, value)
        search(x, y+1, A, B, value)
        search(x, y-1, A, B, value)

    B=[]
    for i in range(len(A)):
        B.append([0 for j in range(len(A[0]))])
    count = 0 
    for i in range(len(A)):
        for j in range(len(A[0])):
            if B[i][j] == 1:
                continue
            search(i, j, A, B, A[i][j])
            count += 1
    return count


A = [[5,4,4], [4,3,4], [3,2,4], [2,2,2], [2,2,2], [3,3,4], [1,4,4], [4,1,1]] 
print(solution(A))