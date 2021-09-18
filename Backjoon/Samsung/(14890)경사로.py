N, L = map(int, input().split())
Map = [list(map(int, input().split())) for i in range(N)]

#cases = [Map[i] for i in range(N)] + list(map(list, zip(*Map)))

answer = 0
visited = []


for i in range(N):
    now = Map[i][0]
    crossable = True
    temp = []

    print(i)
    for j in range(N):
        if Map[i][j] != now:
            # 경사로 놓을 수 있는 지 확인
            if abs(Map[i][j]-now) == 1:
                for k in range(L):
                    if Map[i][j]-now > 0:
                        # 높은 쪽에서 낮은 쪽으로 내려가는 경우
                        l = j+k
                        floor = Map[i][j]
                    else:
                        # 낮은 쪽에서 높은 쪽으로 올라가는 경우
                        l = j-k-1
                        floor = Map[i][j-1]
                    
                    if (0 > l or l >= N) or Map[i][l] != floor or (i, l) in temp:
                            # 경사로 길이를 충족하지 못하거나 이미 경사로를 놓은 곳에 또 넣으려고 하는 경우
                            crossable = False
                            break
                    temp.append((i, l))
                    now = Map[i][j] # 현재 좌표 갱신
            else:
                crossable = False

        if not crossable:
            # 해당 길을 지나갈 수 없는 경우
            break
    else:
        print(temp)
        visited += temp
        answer += 1

print("answer=", answer)
for j in range(N):
    now = Map[0][j]
    crossable = True
    temp = []

    print(j)
    for i in range(N):
        if Map[i][j] != now:
            if abs(Map[i][j]-now) == 1:
                # 경사로 놓을 수 있는 지 확인
                for k in range(L):
                    if Map[i][j]-now < 0:
                        # 높은 쪽에서 낮은 쪽으로 내려가는 경우
                        l = i+k
                        floor = Map[i][j]
                    else:
                        # 낮은 쪽에서 높은 쪽으로 올라가는 경우
                        l = i-k-1
                        floor = Map[i-1][j]
                    
                    if (0 > l or l >= N) or Map[l][j] != floor or (l, j) in temp:    
                            # 경사로 길이를 충족하지 못하거나 이미 경사로를 놓은 곳에 또 넣으려고 하는 경우
                            crossable = False
                            break
                    print(temp)
                    temp.append((l, j))
                else:
                    now = Map[i][j] # 현재 좌표 갱신
            else:
                crossable = False

        if not crossable:
            # 해당 길을 지나갈 수 없는 경우
            break
    else:
        print(temp)
        visited += temp
        answer += 1

print("answer=", answer)
print(visited)
