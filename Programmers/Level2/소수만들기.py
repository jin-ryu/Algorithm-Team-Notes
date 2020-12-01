from itertools import combinations

def prime_numbers(a, b):
    # a, b 사이의 소수 리스트 반환 (에라토스테네스의 체)
    nums = [i for i in range(2, b+1)]
    is_prime = [True] * (b+1)
    result = []
    for n in nums:
        if is_prime[n]:
            # n이 소수라면 n의 배수는 모두 소수가 아닌 것으로 처리
            for i in range(n*2, b+1, n):
                is_prime[i] = False
            if n >= a:
                # a 이상인 수라면 결과 리스트에 추가
                result.append(n)
    return result
                
    
def solution(nums):
    answer = 0
    # 주어진 숫자 중 3개의 수를 더하는 조합
    comb = list(map(sum, combinations(nums, 3)))
    prime = prime_numbers(min(comb), max(comb))

    for c in comb:
        if c in prime:
            answer += 1

    return answer

print(solition([1,2,3,4]))  # 1
print(solition([1,2,7,6,4]))  # 4