def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                # 처음 값이면 이전 레벨의 맨 처음 값을 더해줌
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                # 마지막 값이면 이전 레벨의 마지막 값을 더해줌
                triangle[i][j] += triangle[i-1][j-1]
            else:
                # 중간 값인 경우, 가져올 수 있는 합 중 큰 값을 더해줌
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    answer = max(triangle[-1])

    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))