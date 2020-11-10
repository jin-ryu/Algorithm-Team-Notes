from itertools import combinations

def dfs(x, y, d):
    stack = [(x, y, d)]

    while stack:
        x, y, d = stack.pop()
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            if data[nx][ny] == 'T':
                return False
            # 빈칸인 경우
            if data[nx][ny] == 'X':
                stack.append((nx, ny, d))   # 위치와 탐색방향 추가
    return True

def process():
    for x, y in student:
        for d in range(4):
            if not dfs(x, y, d):    # 이 학생은 막지 못함 
                return False

    return True     # 모든 학생을 막음

n = int(input())
data = []
teacher = []
student = []

for i in range(n):
    data.append(input().split())
    for j in range(n):  # 선생님과 학생들의 좌표를 저장
        if data[i][j] == 'T':
            teacher.append((i, j))
        if data[i][j] == 'S':
            student.append((i, j))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

seen = []
# 선생님의 시야에 있는 빈 칸만 뽑음
for i in range(len(teacher)):
    x, y = teacher[i]
    for j in range(n):
        if data[x][j] == 'X':
            seen.append((x, j))
        if data[j][y] == 'X':
            seen.append((j, y))

seen = list(set(seen))  # 중복 제거


# 시야에 있는 빈칸 중 3개를 뽑음
comb = list(combinations(seen, 3))

for i in range(len(comb)):
    for x, y in comb[i]:    # 벽 설치
            data[x][y] = 'O'    

    if process():
        print("YES")
        break

    for x, y in comb[i]:    # 벽 제거
            data[x][y] = 'X'
else:
    print("NO")
