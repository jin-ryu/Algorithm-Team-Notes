def solution(brown, yellow):
    answer = []
    N = brown + yellow

    # i가 가로길이 j가 세로길이
    for i in range(2, N):
        if N%i != 0:
            continue
        j = int(N/i)
        if i >= j and int((brown-2*i)/2+2) == j:
            answer = [i, j]
            break

    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
print(solution(18, 6))

print(solution(16, 8))