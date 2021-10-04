def solution(s):
    answer = 0
    
    for start in range(len(s)):
        stack = []
        for j in range(len(s)):
            i = (start + j) % len(s)
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif s[i] == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif s[i] == ']' and stack and stack[-1] == '[':
                stack.pop()  
            else: 
                # 올바르지 않은 문자열이 있다면 탐색 종료
                break
            
        else:
            if not stack:
                answer += 1
            
    return answer