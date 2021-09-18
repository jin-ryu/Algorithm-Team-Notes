from itertools import combinations

def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solution(places):
    answer = []
    
    for p in places:
        people = []
        cnt = 0
        
        for i in range(len(p)):
            for j in range(len(p[0])):
                if p[i][j] == 'P':
                    people.append((i,j))
        
        comb = combinations(people, 2)
        for c in comb:
            a, b = c[0], c[1]
            if distance(a, b) <= 2:
                # 파티션 체크
                if a[0] == b[0]:
                    i = a[0]
                    for j in range(min(a[1], b[1]) + 1, max(a[1], b[1])):
                        if p[i][j] == 'X':
                            break
                    else:
                        cnt += 1
                
                elif a[1] == b[1]:
                    j = a[1]
                    for i in range(min(a[0], b[0]) + 1, max(a[0], b[0])):
                        if p[i][j] == 'X':
                            break
                    else:
                        cnt += 1
                elif not (p[a[0]][b[1]] == 'X' and p[b[0]][a[1]] == 'X'):
                    cnt += 1
        
        if cnt == 0:
            answer.append(1)
        else:
            answer.append(0)
        
                
    return answer