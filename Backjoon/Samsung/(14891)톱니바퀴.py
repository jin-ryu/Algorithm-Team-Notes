from collections import deque

arr = [deque(input()) for _ in range(4)]
K = int(input())
order = [list(map(int, input().split())) for _ in range(K)]

def rotate(target, dir):
    if dir == 1:    # 시계방향
        n = target.pop()
        target.appendleft(n)
    elif dir == -1:     # 반시계방향
        n = target.popleft()
        target.append(n)
    
    return target

for num, dir in order:
    # 서로 다른 극인 것 표시
    change = [False]
    for i in range(len(arr)-1):
        if arr[i][2] != arr[i+1][6]:
            change.append(True)
        else:
            change.append(False)

    # 선택한 톱니바퀴 회전
    arr[num-1] = rotate(arr[num-1], dir)
    
    # 왼쪽 이동
    d = dir
    for i in range(num-2, -1, -1):
        if change[i+1]:
            d *= -1
            arr[i] = rotate(arr[i], d)
        else:
            break
    # 오른쪽 이동
    d = dir
    for i in range(num, 4):
        if change[i]:
            d *= -1
            arr[i] = rotate(arr[i], d)
        else:
            break

answer = 0
for i in range(4):
    n = 0
    if arr[i][0] == '1':
        n = 1
    answer += 2**i * n

print(answer)
