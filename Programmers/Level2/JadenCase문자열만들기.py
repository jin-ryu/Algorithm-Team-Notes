def solution(s):
    # 문자열에 공백이 있다면 공백까지 전부 출력해줘야 함
    s = list(s.lower())
    # 첫번째 문자 대문자로 변환
    s[0] = s[0].upper()
    
    for i in range(1, len(s)):
        # 이후 단어의 첫글자가 알파벳이면 대문자로 변환
        if s[i].isalpha() and s[i-1] == ' ':
            s[i] = s[i].upper()
            
    return "".join(s)

print(solution("For     THe   Last      Week"))