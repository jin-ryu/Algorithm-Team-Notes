from bisect import bisect
def solution(info, query):
    answer = []
    scores = []

    # 4가지 항목에 대해 각각 딕셔너리 생성, 안의 리스트에 (지원자, 점수) 값이 들어감
    language = {'cpp': [], 'java': [], 'python': []}
    occupation = {'backend': [], 'frontend': []}
    career = {'junior': [], 'senior': []}
    soulfood = {'chicken': [], 'pizza': []}

    for index in range(len(info)):
        info_list = info[index].split(" ")
        scores.append(int(info_list[-1]))     # 이 사람의 점수

        # 각각 항목을 딕셔너리에 저장
        language[info_list[0]].append(index)
        occupation[info_list[1]].append(index)
        career[info_list[2]].append(index)
        soulfood[info_list[3]].append(index)


    for q in query:
        # 쿼리 분할해 리스트에 저장
        q_list = list(q.split(" and "))  
        last = q_list[-1].split(" ")    # 마지막에 soulfood와 score도 분리
        q_list.pop()
        q_list.extend(last)

        base_score = int(q_list[-1]) # 기준 점수 (x점 이상)
        common_set = set([x for x in range(len(info)) if scores[x] >= base_score])
        common_set = findPerson(q_list[0], language, common_set)
        common_set = findPerson(q_list[1], occupation, common_set)
        common_set = findPerson(q_list[2], career, common_set)
        common_set = findPerson(q_list[3], soulfood, common_set)

        count = len(common_set)  # 4가지 조건을 모두 만족하는 사람의 수 
        answer.append(count)
 
    return answer

def findPerson(condition, dictionary, common_set):   # 조건에 맞는 사람들의 리스트를 반환
    if condition != "-":   # condition에 해당하는 리스트
        return set(dictionary[condition]) & common_set
    return common_set

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))