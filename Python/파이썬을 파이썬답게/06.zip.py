def solution(mylist):
    # zip(*iterables): 딕셔너리를 만들어줌 (튜플 형태)
    # list: 전체를 리스트로 만들어줌
    # map(list, zip()): 안에 있는 인자를 리스트로 만들어줌
    answers=list(map(list, zip(mylist)))
    return answers

mylist = [[1,2,3], [4,5,6], [7,8,9]]
print(solution(mylist))

mylist2 = [[0, 3, 1, 2], [1, 1, 3, 4], [0, 3, 1, 3], [3, 0, 3, 1]]
print(solution(mylist2))