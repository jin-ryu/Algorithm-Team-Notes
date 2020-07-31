# 어떤 과학자가 발표한 논문 n편 중, 
# h번 이상 인용된 논문이 h편 이상이고 
# 나머지 논문이 h번 이하 인용되었다면 
# h의 최댓값이 이 과학자의 H-Index입니다.

# 내가 푼 풀이
def solution(citations):
    n = len(citations)
    for h in reversed(range(n+1)):
        greater = []
        for i in citations:
            if i >= h:
                greater.append(i)
        if len(greater) >= h:
            break
    return h

# 해결 방법1
def solution1(citations):
    citations.sort(reverse=True)
    n = len(citations)

    # h가 리스트의 수를 넘을 수 없으므로 최대 n개
    # citations를 정렬해 놓았기 때문에 citations[i]가 n-i이상이면
    # n-i이상인 citations는 n-i개 (이상)이다
    for i in range(n):
        if citations[i] >= n-i:
            return n-i
               
# 인용 횟수
citations = [3, 0, 6, 1, 5]
print(solution(citations))