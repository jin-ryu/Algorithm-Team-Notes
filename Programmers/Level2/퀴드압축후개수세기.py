# 프로그래머스는 전역변수 사용 불가능
def compress(arr, x, y, size, count_zero, count_one):
    if size == 1:
        return count_zero, count_one
    
    total = sum([arr[i][j] for i in range(x, x+size) for j in range(y, y+size)])
    #  0으로 압축
    if total == 0:
        count_zero -= size**2 - 1
    # 1로 압축
    elif total == size**2:  
        count_one -= size**2 - 1
    else:
        # 4분할 해서 다시 압축 시도
        for i in range(x, x+size, size//2):
            for j in range(y, y+size, size//2):
                count_zero, count_one = compress(arr, i, j, size // 2, count_zero, count_one)
    
    return count_zero, count_one
        
    
def solution(arr):
    new_arr = [arr[i][j] for i in range(len(arr)) for j in range(len(arr[i]))]
    count_one = sum(new_arr)
    count_zero = len(new_arr) - count_one
    
    # 압축 진행
    count_zero, count_one = compress(arr, 0, 0, len(arr), count_zero, count_one)

    return [count_zero, count_one]

print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))