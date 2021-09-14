from itertools import combinations  
from sys import stdin
input = stdin.readline

# 입력
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

def getSum(s, team):
    _sum = 0
    for i in range(len(team)):
        for j in range(i, len(team)):
            x = team[i]
            y = team[j]
            _sum += s[x][y] + s[y][x]

    return _sum

p = [i for i in range(n)]
# 가능한 팀 조합 생성
teams = list(combinations(p, n//2)) 

answer = 1000
m = len(teams)
# 조합은 좌우 대칭이므로 반절만 탐색해도 됨
for i in range(m//2):
    diff = abs(getSum(s, teams[i]) - getSum(s, teams[m-1-i]))
    answer = min(answer, diff)

print(answer)
    



