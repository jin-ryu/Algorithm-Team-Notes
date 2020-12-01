# 분할정복 문제: 우선순위가 낮은 연산자부터 수식을 쪼갠다 (재귀로 들어감)
from itertools import permutations

def calc(priority, i, expression):
    # priority[i] 연산자를 기준으로 수식을 쪼개 계산하는 재귀함수
    if i == 2:
        # 마지막 우선순위까지 쪼갠 경우 결과를 문자열로 반환(다시 수식에 붙이기 위해)
        return str(eval(expression))
    
    # op 기준으로 수식 쪼갬
    op = priority[i]
    ex = expression.split(op)
    # 쪼갠 수식을 다음 op 기준으로 쪼개기 위해 재귀 호출
    # 결과를 합쳐서 다시 수식으로 만듦
    result = op.join([calc(priority, i+1, e) for e in ex])
    
    return str(eval(result))
    
    
def solution(expression):
    answer = 0
    priorities = list(permutations(('+', '-', '*'), 3))
    
    for priority in priorities:
        result = int(calc(priority, 0, expression))
        answer = max(answer, abs(result))
        
    return answer

print(solution("100-200*300-500+20"))   # 60420
print(solution("50*6-3*2")) # 300
