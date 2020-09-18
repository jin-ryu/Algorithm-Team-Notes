from itertools import permutations

def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    perms=[]

    for i in range(1, len(numbers)+1):
        perms = perms + list(map(int, map(''.join, permutations(numbers, i))))
    perms = list(set(perms))    # 중복 제거

    # 소수 개수 체크
    for n in perms:
        if isPrime(n):
            answer += 1

    return answer


numbers1 = "17"
print(solution(numbers1))
numbers2 = "011"
print(solution(numbers2))