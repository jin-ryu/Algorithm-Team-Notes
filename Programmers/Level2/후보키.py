from itertools import combinations

def solution(relation):
    zip_relation = list(zip(*relation))
    cnt = len(relation[0])  # 속성의 개수
    attr = [i for i in range(cnt)]  # 속성 번호
    keys = set()
    
    # 속성 별로 추출함
    for i in range(len(zip_relation)):
        if len(zip_relation[i]) == len(set(zip_relation[i])):
            # 유일성을 가지는 1개짜리 키 추가
            keys.add(i)

    # 1개짜리 키가 있다면 관련 조합은 제거
    attr = [i for i in attr if i not in keys]

    for r in range(2, len(attr)+1):
        comb = list(combinations(attr, r))
        for i in range(len(comb)):
            temp = []
            for j in range(len(comb[i])):
                # i번째 속성 원소들을 뽑아서 추가
                temp.append(zip_relation[comb[i][j]])
            # 각각 원소들을 조합시킴
            temp = list(zip(*temp))
            if len(temp) == len(set(temp)):
                # 유일성을 만족하는 경우
                isMinimal = True
                for k in keys:
                    # type(변수): 변수의 타입을 가져옴
                    # A.issubset(B): A가 B의 부분집합인지 확인
                    if type(k) != int and set(k).issubset(set(comb[i])):
                        isMinimal = False
                if isMinimal:
                    # 최소성을 만족하는 경우
                    keys.add(comb[i])
        
    return len(keys)