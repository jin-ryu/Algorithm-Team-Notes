import copy
import numpy as np

def rotate_90(t):
    n = [[0 for j in range(len(t))] for i in range(len(t[0]))]  # row, col 크기 변경

    for i in range(len(t)):
        for j in range(len(t[0])):
            x = j
            y = len(t)-1-i
            n[x][y] = t[i][j]

    return n

def vertical_symmetry(t):
    if len(t) == 1 or len(t[0]) == 1 or len(t) == len(t[0]):
        # 대칭 시켜도 동일한 경우
        return t
    
    n = [[0 for j in range(len(t[0]))] for i in range(len(t))] 
    for i in range(len(t)):
        for j in range(len(t[0])):
            y = j
            x = len(t)-1-i
            n[x][y] = t[i][j]
    
    return n

def horizontal_symmetry(t):
    if len(t) == 1 or len(t[0]) == 1 or len(t) == len(t[0]):
        # 대칭 시켜도 동일한 경우
        return t
    
    n = [[0 for j in range(len(t[0]))] for i in range(len(t))] 
    for i in range(len(t)):
        for j in range(len(t[0])):
            x = i
            y = len(t[0])-1-j
            n[x][y] = t[i][j]

    return n    

def match(board, t):
    result = 0
    for i in range(len(board)-len(t)+1):
        for j in range(len(board[0])-len(t[0])+1):
            temp = 0
            for x in range(len(t)):
                for y in range(len(t[0])):
                    temp += board[i+x][j+y] * t[x][y]

            result = max(temp, result)
    #print(t, result)    
    return result


def add(tetro, t):
    # 중복 확인 후 추가
    if t not in tetro:
        tetro.append(t)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]

base = [
    [[1, 1, 1, 1]], 
    [[1, 1], [1, 1]],
    [[1, 0], [1, 0], [1, 1]],
    [[1, 0], [1, 1], [0, 1]],
    [[1, 1, 1], [0, 1, 0]]
]

tetro = copy.deepcopy(base)

# tetro 리스트를 따로 빼서 하면 python에서도 맞는 코드
answer = 0
for t in base:
    for _ in range(4):
        t = rotate_90(t)
        add(tetro, t)
        add(tetro, vertical_symmetry(t))
        add(tetro, horizontal_symmetry(t))

        # 백준은 numpy 모듈 지원 안함
        # t = np.rot90(np.array(t))
        # add(tetro, list(map(list, t)))
        # add(tetro, list(map(list, np.flipud(t))))
        # add(tetro, list(map(list, np.fliplr(t))))


for t in tetro:
    answer = max(answer, match(board, t))

print(answer)

