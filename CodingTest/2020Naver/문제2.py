import itertools

empty = -101
def setNowLevel(answer, i, j):
    if j == 0:  # 왼쪽 끝 값일 때
        up = answer[i-1][j]
        right = answer[i][j+1]
        if right != empty:
            answer[i][j] =  up - right

    elif j == i:   # 오른쪽 끝 값일 때
        up = answer[i-1][j-1] 
        left = answer[i][j-1]
        if left != empty:
            answer[i][j] = up - left

    else:   # 중간 값일 때
        if answer[i-1][j-1] != empty:
            up = answer[i-1][j-1]
            left = answer[i][j-1]
            if left != empty:
                answer[i][j] =  upd - left
        if answer[i-1][j] != empty:
            up =  answer[i-1][j]
            right = answer[i][j+1]
            if right != empty:
                answer[i][j] =  up - right

    return answer

def setNextLevel(answer, i, j):
    left = answer[i+1][j]
    right = answer[i+1][j+1]

    if left == empty and right != empty:
        answer[i+1][j] = answer[i][j] -  right
    if right == empty and left != empty:
        answer[i+1][j+1] =  answer[i][j] - left
    
    return answer

def solution(blocks):
    answer = []
    height = len(blocks)    # 피라미드의 높이

    # 피라미드 생성
    for i in range(height):
        answer.append([empty]*(i+1))  # 0으로 초기화

        j, value = blocks[i][0], blocks[i][1]
        answer[i][j] =  value   # 값 추가

    # 값 계산
    for i in range(height):
        for j in range(i+1):
            if answer[i][j] == empty:   # 값이 없는 경우
                answer = setNowLevel(answer, i, j)

            if answer[i][j] != empty and i+1 < height:   # 값이 있는 경우
                answer = setNextLevel(answer, i, j)

    # 마지막 줄만 다시한번 역순으로 진행
    i = height-1
    for j in range(i, -1, -1):
        answer = setNowLevel(answer, i, j)

    return list(itertools.chain.from_iterable(answer))    # 1차원 배열로 변경

print(solution([[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]))
print(solution([[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]))