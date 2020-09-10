def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_order = []    # 선행 스킬 목록들 추가
        for index in range(len(skills)):
            point = len(skill_order)    # 현재 나올 수 있는 스킬 목록을 가리킴
            if point >= len(skill)-1:
                point = len(skill)-1
            # 선행 스킬 목록에 없다면 스킵
            if skills[index] not in skill: 
                continue 
            # 선행 스킬 목록에 있고, 순서에 맞다면 skill order에 추가  
            elif skills[index] in skill and skills[index] == skill[point]:
                skill_order.append(skills[index])
            # 순서가 틀리다면 탈출
            else:   
                break
        else:
            answer += 1 # 순서가 맞다면 개수 하나 증가

    return answer

print(solution("CBD", ["BACDE", "CBADD", "AECB", "BDA"] ))