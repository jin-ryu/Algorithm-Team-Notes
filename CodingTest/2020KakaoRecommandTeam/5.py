import math

MAX_DIST = 2000000000
import bisect
def closest(arr, val):
    ans = (MAX_DIST + 10, "NONE")
    x = bisect.bisect_right(arr, (val, ""))
    if x > 0:
        ans = (arr[x][0] - arr[x-1][0], arr[x-1][1])
    if x < len(arr) - 1:
        alt = (arr[x+1][0] - arr[x][0], arr[x+1][1])
        if alt < ans:
            ans = alt
    return ans

def closestStraightCity(c, x, y, q):
    xs = {}
    ys = {}
    cities = {}

    coord = list(zip(x,y))
    cities = dict(zip(c, coord))
    test =  dict(zip(x,c))
    test2 =  dict(zip(y,c))
    print(test)
    print(test2)

    for i in range(len(c)):
        cities[c[i]] = (x[i], y[i])
        if x[i] not in xs:
            xs[x[i]] = []
        if y[i] not in ys:
            ys[y[i]] = []
            
        xs[x[i]].append((y[i], c[i]))
        ys[y[i]].append((x[i], c[i]))
    
    print(xs)
    print(ys)
    print(cities)
    
    for x in xs:
        xs[x] = sorted(xs[x])
    for y in ys:
        ys[y] = sorted(ys[y])

    ans = []
    for city in q:
        if city not in cities:
            ans.append("NONE")
            continue
        x, y = cities[city]
        print(x, y)
        res = closest(xs[x], y)
        alt = closest(ys[y], x)
        print(res, alt)
        if alt < res:
            res = alt
        ans.append(res[1])
    return ans

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
