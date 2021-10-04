N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]

def backtracking(now, start, numbers):
    if len(now) == M:
        # 결과 출력
        print(' '.join(map(str, now)))
        return
        
    for i in range(start, len(numbers)):
        # 같은 수를 여러 번 골라도 됨
        now.append(numbers[i])
        backtracking(now, i, numbers)   # 비내림차순 조건 추가
        now.pop()

backtracking([], 0, numbers)