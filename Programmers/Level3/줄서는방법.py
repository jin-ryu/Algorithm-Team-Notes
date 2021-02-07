import math

result = []

# 순열 사용해서 모든 방법을 나열하면 시간초과!
def line(n, k, count, position):
    if position > n:
        # n번째 숫자까지 전부 찾은 경우 종료
        return 
    
    for p in people:
        # 현재 position에 맞는 숫자까지 이동     
        fac = math.factorial(n-position)
        if count + fac < k:
            count += fac
            
        else:
            # 삽입한 원소 제거
            people.remove(p)
            # 결과 추가
            result.append(p)
            # 다음 인덱스 번호 찾음
            line(n, k, count, position+1)
   

def solution(n, k):
    global people
    people = [i for i in range(1, n+1)]
    # 줄서는 방법 찾기
    line(n, k, 0, 1)
    
    return result