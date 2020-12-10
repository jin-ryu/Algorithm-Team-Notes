import string

def solution(msg):
    answer = []
    _dict = {}
    
    # 사전 초기화 (key: 단어, value: 색인번호)
    for i, v in enumerate(string.ascii_uppercase):
        _dict[v] = i+1
    
    # 압축 진행
    s, e = 0, 1
    while e <= len(msg):
        while e <= len(msg) and msg[s:e] in _dict.keys():
            # 현재 입력과 일치하는 가장 긴 문자열을 찾음
            e += 1
        
        # 색인 출력
        answer.append(_dict[msg[s:e-1]])
        # 사전 등록
        _dict[msg[s:e]] = len(_dict.keys()) + 1
        # 다음 단어로 이동
        s = e-1
        
    return answer

print(solution("KAKAO"))