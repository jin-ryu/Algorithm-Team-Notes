def isCorrect(arr):
    stack = []
    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append(arr[i])
        elif stack:
            # 스택에 짝을 맞출게 존재
            stack.pop()
        else:
            # 스택이 비어 있다면 false
            return False
    
    if stack:
        # 모든 매칭 후에 스택에 남아있는게 있다면 false
        return False
    return True

n = int(input())
for i in range(n):
    arr = input()
    if isCorrect(arr):
        print("YES")
    else:
        print("NO")
