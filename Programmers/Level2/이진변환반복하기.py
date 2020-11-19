def solution(s):
    count, delete = 0, 0
    while s != '1':
        zero = s.count('0')
        if zero != 0:
            # 0 제거
            delete += zero
            s = s.replace('0', '')
        # 제거된 문자열의 길이를 2진법으로 표현한 문자열로 변환
        n = len(s)
        s = bin(n)[2:]
        # 이진 변환 횟수 증가
        count += 1
    
    return [count, delete]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
