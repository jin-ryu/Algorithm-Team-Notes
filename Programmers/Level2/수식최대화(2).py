# 연산자와 숫자 분리해서 푸는 방법
from itertools import permutations
import copy

def split_num(expression, types):
    # 숫자 분리
    for op in types:
        expression = expression.replace(op, " ")
    numbers = list(expression.split(" "))
    
    return numbers

def solution(expression):
    answer = 0
    ops = ('+', '-', '*')
    # 연산자와 피연산자 분리
    operators = [e for e in expression if e in ops]
    types = list(set(operators))
    numbers = split_num(expression, types)
    
    # 우선순위 정함
    priorities = list(permutations(types, len(types)))
    for priority in priorities:
        temp_op = copy.deepcopy(operators)
        temp_num = copy.deepcopy(numbers)
        for i in range(len(priority)):
            op = priority[i]
            while op in temp_op:
                # 아직 처리해야할 op가 남아있는 동안 반복
                j = temp_op.index(op)
                # 중간 결과 반영
                sub = str(eval(temp_num[j] + temp_op[j] + temp_num[j+1]))
                temp_num[j] = sub
                del temp_num[j+1]
                del temp_op[j]
        
        answer = max(answer, abs(int(temp_num[0])))
            
        
    return answer

print(solution("100-200*300-500+20"))   # 60420
print(solution("50*6-3*2")) # 300