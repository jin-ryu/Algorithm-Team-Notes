import sys

def isVPS(string):
    # 올바른 괄호 문자열인지 확인
    stack = []

    for ch in string:
        if ch == '(':
            stack.append(ch)
        elif stack:
            stack.pop()
        else:
            # 짝이 없는 경우
            return False
    if stack:
        # 짝을 찾지 못한 문자가 남았다면
        return False
 
    return True

n = int(sys.stdin.readline())
for _ in range(n):
    # 이렇게 입력 받은 경우 개행 문자가 넘어감
    string = sys.stdin.readline()
    if isVPS(string[:-1]):
        print("YES")
    else:
        print("NO")

