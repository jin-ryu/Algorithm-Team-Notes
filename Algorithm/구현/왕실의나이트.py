def solution(location):
    directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2) ]
    x = ord(str(location)[0]) - ord('a') + 1    
    y = int(str(location)[1])
    count = 0

    for direction in directions:
        new_xdir = x + direction[0]
        new_ydir = y + direction[1]
        
        if new_xdir < 1 or new_xdir > 8 or new_ydir < 1 or new_ydir > 8:
            continue
        count += 1

    return count 

print(solution("a1"))   # 2
print(solution("c2"))   # 6
print(solution("d4"))   # 8