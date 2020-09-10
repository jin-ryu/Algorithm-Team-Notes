import math
def solution(w,h):
    # 최대공약수가 1보다 작을때 잘라지는 사각형의 개수: w+h-1(겹치는 사각형)
    # 최대공약수가 1보다 클때: (최대공약수 * 위의 개수) = g(w//g + h//g -1) = w+h-g  
    
    # 전체 사각형 개수 - 잘라지는 사각형의 개수 = w*h - (w+h-g)
    return w*h - (w+h-math.gcd(w,h))


print(solution(8, 12))