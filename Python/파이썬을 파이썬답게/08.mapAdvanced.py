def solution(mylist):
    answer = list(map(len, mylist))
    return answer

mylist = [[1], [2]]
print(solution(mylist))

mylist2 = [[1, 2], [3, 4], [5]]
print(solution(mylist2))