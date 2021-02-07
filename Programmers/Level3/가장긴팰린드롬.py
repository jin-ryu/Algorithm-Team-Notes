def palindrome(s):
    # 좌우 대칭인지 확인
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    
    return True
        
def solution(s): 
    for length in reversed(range(1, len(s)+1)):
        # 길이를 전체 길이부터 1까지
        for start in range(len(s)-length+1):
            # 시작 위치는 처음부터 길이 뺀것 만큼
            if palindrome(s[start:start+length]):
                return len(s[start:start+length])
                
print(solution("abccbefdsdfe"))