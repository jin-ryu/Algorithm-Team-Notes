def solution(s):
    answer = s
    length = len(s)

    for unit in range(1, length//2+1):  # 문자열을 자를 단위
        word = ""   # unit 단위로 압축된 단어 
        count = 1
        for i in range(0, length, unit):
            # 문자열을 unit 단위로 잘라서 앞 뒤를 비교    
            front = s[i:i+unit] 
            back = s[i+unit:i+(unit*2)]
            
            if front == back:   
                count += 1
            else:
                if count == 1:
                    word += front
                else:
                    word += str(count) + front
                count = 1   # 반복되는 단어가 없으므로 count 초기화

        # 최소 길이 단어를 answer에 넣음
        if len(word) < len(answer):
            answer = word

    return len(answer)


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
