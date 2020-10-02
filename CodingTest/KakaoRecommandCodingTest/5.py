import math

MAX = 2000000000
import bisect
def closest(arr, val):
    answer = (MAX + 10, "NONE")
    x = bisect.bisect_right(arr, (val, ""))
    if x > 0:
        answer = (arr[x][0] - arr[x-1][0], arr[x-1][1])
    if x < len(arr) - 1:
        alt = (arr[x+1][0] - arr[x][0], arr[x+1][1])
        if alt < answer:
            answer = alt
    return answer

def closestStraightCity(c, x, y, q):
    xs = {}
    ys = {}
    cities = {}

    for i in range(len(c)):
        cities[c[i]] = (x[i], y[i])
        if x[i] not in xs:
            xs[x[i]] = []
        if y[i] not in ys:
            ys[y[i]] = []
            
        xs[x[i]].append((y[i], c[i]))
        ys[y[i]].append((x[i], c[i]))
    
    for x in xs:
        xs[x] = sorted(xs[x])
    for y in ys:
        ys[y] = sorted(ys[y])

    answer = []
    for city in q:
        if city not in cities:
            answer.append("NONE")
            continue
        x, y = cities[city]
        res = closest(xs[x], y)
        alt = closest(ys[y], x)
        if alt < res:
            res = alt
        answer.append(res[1])
    return answer

n = 3
c=['c1', 'c2', 'c3']
x=[3,2,1]
y=[3,2,3]
q =['c1', 'c2', 'c3']

print(closestStraightCity(c, x, y, q))








def closestStraightCity1(c, x, y, q):
    # Write your code here
    answer = []
    coord = list(zip(x,y))
    _dict = dict(zip(c, coord))
    

    for name in q:
        mins = float('inf')
        minName = 'NONE'
        for key, coord in _dict.items():
            x1, y1 = _dict[name]   # 이 좌표와 근접한 좌표
            x2, y2 = coord
            length = float('inf')

            if x1 != x2 and y1 != y2:
                continue
            elif x1 == x2:
                length = abs(y1-y2)
            elif y1 == y2:
                length = abs(x1-x2)
                
            if length < min:
                min = length
                minName = key

        answer.append(minName)
        min = float('inf')
    return answer
