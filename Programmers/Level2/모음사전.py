from itertools import product

def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    arr = []
    
    for i in range(1, 6):
        # 중복 순열
        arr += list(map("".join, list(product(alphabet, repeat = i))))
        
    arr.sort()
    
    return arr.index(word)+1


# product 안쓰는 풀이 - 숫자 연산이라 효율이 훨씬 좋음
def solution(word):
    answer = 0
    for i, n in enumerate(word):
        # (i번째 숫자로 만들 수 있는 마지막 인덱스) / (글자수가 5개이므로 4 영역으로 분할) * 글자의 순번 + 1(인덱스가 아닌 순번이므로)
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1

    return answer