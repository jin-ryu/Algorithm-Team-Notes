import bisect

n = int(input())
a = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

def isContain(a, num):
    # num이 a 안에 있는지 이진 탐색으로 확인
    # in 연산자는 이진 탐색보다 느림
    if bisect.bisect_left(a, num) < bisect.bisect_right(a, num):
        return True

    return False


a.sort()    # a 정렬
for num in numbers:
    if isContain(a, num):
        print(1)
    else:
        print(0)

