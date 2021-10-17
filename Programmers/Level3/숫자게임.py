def solution(A, B):
    answer = 0

    A.sort(reverse=True)
    B.sort(reverse=True)
    
    while B:
        if A[-1] < B[-1]:
             # A의 가장 작은 수 < B의 가장 작은 수 == B 승리 가능
            answer += 1
            A.pop()
        B.pop()
        
    return answer