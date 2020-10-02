from itertools import product

def solution(k):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    # 숫자들
    counts = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6] # 숫자별 필요한 성냥개비 개수
    answer =  0    # 성냥개비로 만들 수 있는 가짓수

    for r in range(1, k//2+1): 
        perms = list(set(product(numbers, repeat=r)))   # 중복 순열 (같은 값은 제외)
        if r != 1:  # 1의자리 수가 아니면 0으로 시작하는 경우 제외
            perms = [p for p in perms if p[0] != 0]
    
        for i in range(len(perms)): # k와 합이 같으면 카운트
            s = sum([counts[perms[i][j]-1] for j in range(len(perms[i]))])
            if s == k:
                answer += 1

    return answer


print(solution(5))
print(solution(6))
print(solution(11))
print(solution(1))


