from collections import Counter

def solution(N, stages):
    answer = []
    n = len(stages)
    
    counter = Counter(stages).most_common() # 개수 파악
    counter.sort()  # stage 순으로 졍럴
    
    prev = 0    # 현재 스테이지에 도달하지 못한 사람 수
    for i in range(len(counter)):
        stage, fail = counter[i]
        if stage == N+1:    # 스테이지 클리어 한 사람들을 만나면 종료
            break   
        total = n - prev    # 스테이지에 도달한 사람들
        answer.append((stage, fail/total))
        prev += fail   
        
    answer.sort(key=(lambda x:(-x[1], x[0])))    # 실패율 순으로 정렬
    
    for i in range(len(answer)):    # 스테이지 번호만 추출
        answer[i] = answer[i][0]
    
    # 실패율이 0인 스테이지 추가
    no_stage = list(set([i for i in range(1, N+1)]) - set(answer))
    no_stage.sort()
    answer.extend(no_stage)
    
    return answer