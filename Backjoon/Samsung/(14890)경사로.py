N, L = map(int, input().split())
Map = [list(map(int, input().split())) for i in range(N)]

def solve(N, L, Map):
    result = 0

    for i in range(N):
        l, r = 0, 1
        count = 0
        isOkay = True
        while r < N:
            if Map[i][l] == Map[i][r]:
                r += 1
                count += 1
            elif count == L+1 and abs(Map[i][l] - Map[i][r]) == 1:
                l = r
                r += 1
                count = 0
                continue
            else:
                isOkay = False
                break
        
        if isOkay:
            result += 1
    
    return result

print(solve(N, L, Map))    
print(solve(N, L, list(map(list, zip(*Map)))))       

# m = list(map(list, zip(*Map)))