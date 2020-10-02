import itertools
from functools import reduce
import operator
import numpy as np

def solution(mylist):
    # 방법1(worst) - sum 함수 
    answer1 = sum(mylist, [])

    # 방법2 - itertools.chain.from_iterable
    answer2 = list(itertools.chain.from_iterable(mylist))
    
    # 방법3 - itertools와 unpacking
    answer3 =  list(itertools.chain(*mylist))

    # 방법4 - list comprehension 이용
    answer4 = [element for array in mylist for element in array]

    # 방법5 - reduce 함수 이용 1
    answer5 = list(reduce(lambda x, y: x+y, mylist))
    
    # 방법6 - reduce 함수 이용 2
    answer6 = list(reduce(operator.add, mylist))

    # 방법7(best) - numpy 라이브러리의 flatten 이용
    answer7 = np.array(mylist).flatten().tolist()
    
    return answer1, answer2, answer3, answer4, answer5, answer6, answer7

mylist = [[1, 2], [3, 4], [5, 6]]
print(solution(mylist))