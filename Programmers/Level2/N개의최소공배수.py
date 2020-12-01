import math
# math 라이브러리에 gcd는 있지만 lcm은 없다

def lcm(a, b):
    # a*b = gcd(a,b) * lcm(a,b) 이용
    return a*b // math.gcd(a, b)

def solution(arr):
    answer = arr[0]
    for num in arr:
        # 두수의 최소공배수의 최소공배수를 구함
        answer = lcm(answer, num) 

    return answer

print(solution([2,6,8,14])) # 168
print(solution([1,2,3]))    # 6