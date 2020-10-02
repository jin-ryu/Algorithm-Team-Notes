# 재귀함수
def solution(p):
    answer = ''
    left_count, right_count = 0, 0      # "("의 개수, ")"의 개수
    start, index = 0, 0       # 균형잡힌 괄호 문자열을 분리하기 위한 인덱스
    u, v = "", ""   # 더이상 분리 할 수 없는 균형 문자열, 이후 문자열

    if not p:   # 입력이 빈 문자열인 경우, 빈 문자열을 반환
        return p

    for index in range(len(p)):
        if p[index] == "(" :
            left_count += 1
        else:
            right_count += 1
    
        if left_count == right_count:   # 균형잡힌 괄호 문자열 분리
            u = p[start:index+1]
            v = p[index+1:]

            if u[0] == "(":     # 올바른 괄호 문자열인 경우
                s = solution(v)
                return u + s
                
            else:               # 올바른 괄호 문자열이 아닌 경우
                u = u[1:-1]     # u의 첫 번째와 마지막 문자를 제거
                answer = "(" + solution(v) + ")"
                for i in u:  # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
                    if i =="(":
                        answer += ")"
                    else:
                        answer += "("
                return answer
                
            left_count, right_count = 0, 0  # 카운트 초기화
            start = index + 1  

print(solution("(()())()"))     # "(()())()"
print(solution(")("))           # "()"
print(solution("()))(())((()"))     # "()(())()"
