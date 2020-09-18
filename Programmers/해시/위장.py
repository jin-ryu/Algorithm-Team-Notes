def solution(clothes):
    answer = 1
    N = len(clothes)

    dic = {}
    for i in range(0, N):
        if clothes[i][1] not in dic.keys():     # 옷 종류를 키로 생성
            dic[clothes[i][1]] = [clothes[i][0]]    
        else:
            dic[clothes[i][1]] = dic[clothes[i][1]] + [clothes[i][0]]

    vals = list(dic.values())
    # 입을 수 있는 옷 종류의 수 = 각 종류 별로 선택할지 안할지 여부(+1)를 포함하여 곱해줌
    # ex) A(a,b,c) -> A에서 a/b/c/X 4가지 경우가 나옴 
    # -1은 아무것도 선택하지 않는 경우는 없으므로 제외
    for v in vals:
        answer *= len(v) + 1
    
    return answer - 1


clothes1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes1))
clothes2 = [["crow_mask", "face"], ["black_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes2))
print(solution(clothes1 + clothes2))