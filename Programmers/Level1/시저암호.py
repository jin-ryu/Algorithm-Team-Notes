def solution(s, n):
    answer = ''

    for i in range(len(s)):
        if s[i] != ' ': # 공백이 아닌 경우만 시저 암호화 함
            num = ord(s[i]) + n    
            if ord('A') <= ord(s[i]) <= ord('Z') and num > ord('Z'):   # 대문자인 경우
                num -= ord('Z') - ord('A') + 1
            elif ord('a') <= ord(s[i]) <= ord('z') and num > ord('z'):   # 소문자인 경우
                num -= ord('z') - ord('a') + 1

            answer += chr(num)  # 아스키코드 문자로 변환
        else:
            answer += ' '
            
    return answer

# 좋은 풀이
def answer(s, n):
    count = 26  # 알파벳 개수
    s = list(s) # 리스트로 변환

    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % count + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % count + ord('a'))

    return "".join(s)


print(solution("AB", 1))    # BC
print(solution("z", 1))     # a
print(answer("a B z", 4)) # e F d
