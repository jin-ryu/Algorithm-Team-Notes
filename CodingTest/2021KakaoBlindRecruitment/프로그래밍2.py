from itertools import combinations

def solution(orders, course):
    answer = []
    candidate = {}  # 코스에 추가될 수 있는 후보군들 저장
    
    for r in course:
        candidate[r] = [] 

    for order in orders:    # 각각의 주문으로부터 만들 수 있는 조합을 생성
        for r in course:    # r조합을 생성
            comb = list(map("".join, (map(sorted, map(list, combinations(order, r))))))  # 조합을 알파벳 순으로 정렬하여 XW, WX를 같은 것으로 만듦
        
            if comb:    # 생성된 조합이 있다면 조건에 맞는지 확인
                maxCourses = maxCandidatde(comb, orders)
                for maxCourse in maxCourses:
                    if maxCourse not in candidate[r]:
                        candidate[r].append(maxCourse)
 
    # candidate 리스트에서 가장 많이 주문된 조합을 선정해 answer에 추가    
    for r in course:
        max_count = 0
        r_list = candidate[r]
        if r_list:
            max_count = max(r_list, key= lambda x: x[1])[1] 

        if max_count != 0:
            for index in range(len(r_list)): # 가장 많이 주문된 조합을 찾아서 answer에 추가
                if r_list[index][1] == max_count:    
                    answer.append(r_list[index][0])
    
    answer.sort()   # 알파벳 오름차순 정렬
                
    return answer

def maxCandidatde(comb, orders): 
    candidate = []
    max_count = 0

    for course in comb:  # 조합으로 나온 값들 중 후보 기준에 부합하는 것만 answer에 추가
        count = 0
        for order in orders:
            for menu in course:
                if menu not in order:  # 조합안의 문자 중 하나라도 order에 없으면 다음 조합으로 넘어감
                    break       
            else:
                count += 1  # 조합안에 모든 문자가 있는 경우 카운트 증가

        if (count >= 2) : # 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함
            candidate.append([course, count])

        if max_count < count:
            max_count = count

    # max_count 개수를 가진 조합을 반환
    answer = []
    for index in range(len(candidate)):
        if candidate[index][1] == max_count:
            answer.append(candidate[index])

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))

print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))

