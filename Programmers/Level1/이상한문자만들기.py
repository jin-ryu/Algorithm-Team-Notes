def solution(s):
    s = s.split(" ")   # 공백 기준으로 리스트 분할
    
    for i in range(len(s)): 
        ss = list(s[i])
        for j in range(len(ss)):
            if j%2 == 0 and ss[j].islower():    # 짝수 인덱스 -> 대문자
                ss[j] = chr(ord(ss[j]) - ord('a') + ord('A'))  
            elif j%2 == 1 and ss[j].isupper():           # 홀수 인덱스 -> 소문자
                ss[j] = chr(ord(ss[j]) - ord('A') + ord('a'))  

        s[i] = "".join(ss)
    
    return " ".join(s)

print(solution("try hello world"))  # TrY HeLlO WoRlD
