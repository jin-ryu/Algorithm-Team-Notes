N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]

def backtracking(now, numbers):
    if len(now) == M:  
        # 결과 출력
        print(' '.join(map(str, now)))
        return
        
    for i in range(len(numbers)):
        # 같은 수를 여러 번 골라도 됨
        now.append(numbers[i])
        backtracking(now, numbers)
        now.pop()

backtracking([], numbers)
