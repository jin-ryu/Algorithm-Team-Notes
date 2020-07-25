import operator
#[?] n명의 점수 중에서 80점 이상인 점수의 합계

# 합계 알고리즘(Sum Algorithm): 주어진 범위에 주어진 조건에 해당하는 자료들의 합계

#[1] Input(입력) :  n명의 점수
scores = [100, 75, 50, 37, 90, 95]
total = 0             # 합계가 저장될 그릇
N = len(scores)     # 의사코드(슈도코드)


#[2] Process(처리) : 합계 알고리즘 영역: 주어진 범위에 주어진 조건(필터링)
for i in range(N):          # 주어진 범위
    if scores[i] >= 80:     # 주어진 조건
        total += scores[i]    # SUM

#[3] Ouput(출력)
print(f"{N}명의 점수 중에서 80점 이상의 총점: {sum}")



#[!] My code
result = [score for score in scores if score>= 80]      # list comprehension
print("{}명의 점수 중에서 80점 이상의 총점: {}".format(len(scores), sum(result)))


#[!] 디버거를 사용하여 디버깅 하기
# F9(중단점 설정) -> F5(디버깅 모드) -> F11(한 줄씩 실행) -> F5(마무리)
# 조사식으로 원하는 값, 조건을 확인해볼 수 있음

