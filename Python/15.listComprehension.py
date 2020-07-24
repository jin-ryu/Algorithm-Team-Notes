def solution(mylist):
    # list comprehension
    # [ ( 변수를 활용한 값 ) for ( 사용할 변수 이름 ) in ( 순회할 수 있는 값 ) (*조건문)]
    answer = [i**2 for i in mylist if i%2==0]
    return answer

mylist = [3, 2, 6, 7]
print(solution(mylist))