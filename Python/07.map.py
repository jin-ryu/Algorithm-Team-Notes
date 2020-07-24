def solution(mylist):
    # map: 리스트 or 튜플의 모든 원소에 같은 함수 적용시킴
    answer = list(map(int, mylist))
    return answer

mylist = ['1', '100', '33']
print(solution(mylist))