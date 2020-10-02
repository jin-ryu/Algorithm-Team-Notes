# 완전 탐색
# [중요]  문자열 길이가 N일 때, 길이가 N/2 보다 크게 잘랐을 때는 길이가 줄지 않습니다

def solution(s):
    answer = []     # 압축된 문장의 길이를 저장

    if len(s) == 1: # 문자열의 길이가 1이면 압축 불가능
        return len(s)

    for n in range(1, len(s)//2 + 1): # 압축 단위 크기를 늘려가면서 길이를 계산
        count = 0   # 단위 블록이 반복되는 횟수 
        compressed = ""     # 압축된 문장
        search_block = s[0 : n]  # 압축할 단위 블록

        for start in range(0, len(s), n): 
            block = s[start : start+n]  # 현재 보고 있는 블록(인덱스 넘어가도 문제 없는 듯)
  
            if search_block == block:
                count += 1
            else:
                if count > 1:   # 압축된 단어 더해줌
                    compressed += str(count) + search_block     
                else:   # 압축이 안되었다면 그대로 더해줌
                    compressed += search_block  

                count = 1   # 자기 자신이 있으므로 count는 1부터
                search_block = block  # 다음 블록을 단위 블록으로 바꿔줌

        if count > 1:   # 압축된 단어 더해줌
            compressed += str(count) + search_block     
        else:    # 마지막에 남는 문자열은 그대로 붙여줌
            compressed += s[start:]         
        answer.append(len(compressed))

    return min(answer)

print(solution("aabbaccc"))  # 7
print(solution("ababcdcdababcdcd"))  # 9
print(solution("abcabcdede"))  # 8
print(solution("abcabcabcabcdededededede"))  # 14
print(solution("xababcdcdababcdcd"))  # 17

print(solution("a"))  # 런타임에러 나왔던것
