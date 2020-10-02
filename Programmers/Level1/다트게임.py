# 점수|보너스|[옵션]으로 이루어진 문자열 3세트.
def solution(dartResult):
    answer = []     # 각각의 기회에서 얻은 점수를 리스트로 저장
    score = 0      

    for result in dartResult:
        if result.isdecimal(): # 숫자인지 판별하여 score에 임시 저장
            score = score*10 + int(result)  

        elif result == "*":     # "*"이면 바로 전에 얻은 점수와 이번 점수에 2배
            answer[-1] *= 2
            if len(answer) >= 2:
                answer[-2] *= 2
                
        elif result == "#":     # "#"이면 이번에 얻은 점수에 -1배 
            answer[-1] *= -1
 
        else:  # 보너스라면 숫자 계산
            # "S"는 1승으로 원래 숫자랑 동일하므로 생략
            if result == "D":
                score = score**2
            elif result == "T":
                score = score**3
            answer.append(score)    
            score = 0       # 다음 기회의 점수를 저장하기 위해 초기화
    print(answer)

    return sum(answer)


print(solution("1S2D*3T"))  # 37
print(solution("1D2S#10S")) # 9
print(solution("1D2S0T"))   # 3
print(solution("1S*2T*3S")) # 23
print(solution("1D#2S*3S")) # 5 
print(solution("1T2D3D#"))  # -4
print(solution("1D2S3T*"))  # 59
