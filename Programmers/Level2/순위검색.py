from itertools import combinations
import bisect

def get_keys(p):
    keys = []
    
    for i in range(5):
        comb = combinations([0, 1, 2, 3], i)
        for c in comb:
            temp = ''       # 리스트는 키값이 될 수 없으므로 string으로 키값을 만듦
            for j in range(len(p)):
                if j in c:
                    temp += '-'
                else:
                    temp += p[j]
            keys.append(temp)
            
    return keys

def solution(info, query):
    answer = []
    scores = {}     # key: 검색 조건, value: 조건에 맞는 지원자의 점수
    
    # 검색 조건에 따른 지원자들의 점수 딕셔너리 생성
    for i in info:
        data = i.split()
        s = int(data[4])
        keys = get_keys(data[:4])
    
        for k in keys:
            if k in scores.keys():
                scores[k].append(s)
            else:
                scores[k] = [s]
    
    # 이진탐색을 위한 리스트 정렬
    for key in scores.keys():
        scores[key].sort()
    
    # 쿼리 진행
    for q in query:
        q = q.split()
        key = q[0] + q[2] + q[4] + q[6] 
        
        if key in scores.keys():
            idx = bisect.bisect_left(scores[key], int(q[7]))
            answer.append(len(scores[key]) - idx)   # 슬라이싱 쓰면 O(N)
        else:
            answer.append(0)
                
                
    return answer