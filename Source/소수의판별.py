import math

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    # 제곱수 = 가운데 약수, 나머지는 대칭
    for i in range(1, math.sqrt(x)):
        if x%i == 0:
            return False # 소수가 아님
        
    return True      # 소수임

print(is_prime_number(4))   # 4는 소수가 아님
print(is_prime_number(7))   # 7은 소수임