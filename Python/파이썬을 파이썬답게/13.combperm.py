import itertools

def solution(mylist):
    answer = list(map(list, itertools.permutations(sorted(mylist))))
    return answer

mylist = [2, 1]
print(solution(mylist))

mylist2 = [1, 2, 3]
print(solution(mylist2))