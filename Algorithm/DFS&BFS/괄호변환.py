# "균형잡힌 괄호 문자열"의 인덱스 반환 (정답코드 참조)
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == LEFT:
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

    return p[:i+1], p[i+1:]

def isRight(u): # u가 올바른 문자열인지 확인
    stack = []
    
    for i in range(len(u)):
        if u[i] == LEFT:
            stack.append(u[i])
        elif stack:
            stack.pop()     # 짝이 맞았음
        else:   
            return False    # RIGHT인데 stack이 비어있는 경우는 올바르지 않음
    return True     

def process(u):
    if not u:   # 빈 문자열이라면 반환
        return u
    
    n = len(u)
    u = u[1:n-1]    # 처음과 끝 제거
    
    u = list(u) # 문자열을 할당이 안되므로 리스트로 변경
    for i in range(len(u)): # 문자열 괄호 방향 뒤집기
        if u[i] == LEFT:
            u[i] = RIGHT
        else:
            u[i] = LEFT

    return "".join(u)

def solution(p):
    if not p:   # 빈 문자열인 경우 빈 문자열을 반환
        return p
    
    global LEFT, RIGHT
    LEFT = '('
    RIGHT = ')'
    answer = ''
    
    # 균형잡힌 괄호 문자열 u, v로 분리
    i = balanced_index(p)
    u = p[:i+1]
    v = p[i+1:]

    # 이 부분 재귀적으로 수행하는 게 어려움    
    if isRight(u):
        answer = u + solution(v)     # 올바른 괄호 문자열이라면 v에 대해 다시 수행
    else:
        answer = LEFT + solution(v) + RIGHT + process(u)    # u가 올바른 문자열이 아니라면 변경
        
    return answer