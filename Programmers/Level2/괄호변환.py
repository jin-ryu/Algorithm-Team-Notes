def isCorrect(s):
    # 올바른 문자열인지 확인하는 함수
    stack = []
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else: 
            if stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    
    return True

def reverse(s):
    # 문자열의 괄호 방향 뒤집기
    result = ""
    
    for i in s:
        if i == '(':
            result += ')'
        else:
            result += '('
            
    return result

def divide(w):
    # 빈 문자열인 경우 빈문자열 반환
    if w == "": 
        return w
    
    # 균형잡힌 문자열 u, v로 분리
    lcnt, rcnt = 0, 0

    for i in range(len(w)):
        if w[i] == '(':
            lcnt += 1
        else:
            rcnt += 1
            
        if lcnt == rcnt:
            u, v = w[:i+1] , w[i+1:]
            #print(u, v)
            
            if isCorrect(u):
                return u + divide(v)
            else:
                return '(' + divide(v) + ')' + reverse(u[1:len(u)-1])

def solution(p):
    answer = divide(p)
    return answer

print(solution("()))((()"))