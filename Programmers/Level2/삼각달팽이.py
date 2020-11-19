def solution(n):
    answer = [[0]*(i+1) for i in range(n)]  # 0으로 삼각형 초기화
    N = sum([len(answer[i]) for i in range(n)])
    DOWN, RIGHT, UP =  1, 2, 3
    i, j = 0, 0     # 좌표 초기화
    current = DOWN
    
    
    for x in range(1,N+1):
        answer[i][j] = x
        if current == DOWN:
            i += 1
            if i >= n or answer[i][j]:
                i -= 1  # 인덱스 범위 정상화
                j += 1  # 다음 칸으로 이동
                current = RIGHT
        elif current == RIGHT:
            j += 1
            if j >= n or answer[i][j]:
                i -= 1  # 다음칸으로 이동
                j -= 2  # 인덱스 범위 정상화 + 다음칸으로 이동
                current = UP
        else:
            i -= 1
            j -= 1
            if i <= 0 or answer[i][j]:
                i += 2  # 인덱스 범위 정상화 + 다음칸으로 이동
                j += 1  # 인덱스 범위 정상화
                current = DOWN
    
    # list comprehesion으로 2차원 리스트 1차원으로 변경
    return [answer[i][j] for i in range(len(answer)) for j in range(len(answer[i]))]

print(solution(4))
print(solution(5))
print(solution(6))