from itertools import product

def solution(n, t, m, p):
    # 한자리 숫자 리스트 생성
    digits = [str(i) for i in range(10)]
    digits.extend(['A', 'B', 'C', 'D', 'E', 'F'])
    # 진법에 맞게 digits 변경
    digits = digits[:n]
    
    process = ''
    r = 1
    while len(process) < t*m:
        # 튜브가 t개를 말하기까지 진행과정 
        perm = list(product(digits, repeat = r))
        if r != 1:
            # 두자리 이상인 수부터 0으로 시작하는 거는 제외
            perm = [perm[i] for i in range(len(perm)) if perm[i][0] != '0']
        
        # 진행과정 붙이기
        for i in range(len(perm)):
            process += "".join(perm[i])
        # 조합 자리수 증가
        r += 1
    
    # 결과 계산
    answer = ''
    for i in range(p-1, t*m, m):
        answer += process[i]
        
    return answer