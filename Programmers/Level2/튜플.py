def solution(s):
    answer = []
    s_list = []
    start = 0
    # 문자열 리스트로 바꾸기
    for i in range(1, len(s)-1):
        if s[i] == "{":
            start = i+1
        elif s[i] == "}":
            temp = list(map(int, s[start:i].split(",")))
            s_list.append(temp)
    
    # 리스트 길이 순으로 정렬
    s_list.sort(key=lambda x: len(x))
    
    for i in s_list:
        # 아직 answer에 없는 숫자들만 삽입
        num = [x for x in i if x not in answer]
        answer.extend(num)
    return answer