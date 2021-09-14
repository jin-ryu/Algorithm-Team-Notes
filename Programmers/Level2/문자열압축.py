def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2+1):   # 단위 문자열의 길이
        result = ""
        previous = ""   # 이전 단위 문자열
        count = 0       # 이전 단위 문자열의 개수
        
        for j in range(0, len(s), i):
            now = s[j: j+i]
            
            if not previous or previous == now:
                count += 1
            else:
                if count > 1:
                    result += str(count) + previous
                else:
                    result += previous
                
                count = 1   
                
            previous = now  # 현재 문자열을 이전 문자열로 변경
          
        # 남은 문자열 정리
        if count > 1:
            result += str(count) + previous
        else:
            result += previous
        
        # 최소 길이 갱신
        answer = min(answer, len(result))
        
    return answer


print(solution("aabbaccc"))
print(solution("abcabcabcabcdededededede"))