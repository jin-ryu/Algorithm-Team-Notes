def solution(s):
    # 스택을 이용하면 O(N)시간에 처리 가능하다고 함
    # 문자의 중복을 처리할 때는 스택을 사용하면 유리!!! 
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            # 스택의 top이 현재 보는 문자와 같다면 pop
            stack.pop()
        else:
            # 아니라면 스택에 삽입
            stack.append(i)
            
    if stack:
        # 스택에 문자가 남아있다면 성공적으로 수행할 수 없음
        return 0
    return 1



def old_solution(s):
    answer = 1
    start = 0
    
    while s:
        # 빈 문자열이 아닌 동안 반복
        for i in range(start, len(s)-1):
            if s[i] == s[i+1]:
                # 2개 붙어 있는 짝 제거
                arr = s[i] + s[i+1]
                s = s.replace(arr, "")
                # 반복 횟수 줄이기 위해 설정
                if i > 0:
                    start = i-1
                break
        else:
            # 2개 붙어 있는 짝이 더 이상 없는 경우
            answer = 0
            break
            
    return answer


print(solution("baabaa"))    # 1
print(solution("cdcd"))     # 0