def solution(A):
    N = len(A)

    # 부분 리스트 생성
    subs = []
    for i in range(N):
        for j in range(i+1, N+1):
            subs.append(A[i:j])

    # 등차수열인지 확인
    count = 0
    for sub in subs:
        if len(sub) < 3:
            continue
        v = sub[1] - sub[0]
        for i in range(len(sub)-1):
            if v != sub[i+1] - sub[i]:
                break
        else:
            count += 1

    return count

A = [-1,1,3,3,3,2,3,2,1,0]
print(solution(A))
