def solution(record):
    answer = []
    user = {}
    
    for r in record:
        r = r.split()
        
        if r[0] == "Enter":
            user[r[1]] = r[2]
            answer.append([r[1], "님이 들어왔습니다."])
        elif r[0] == "Leave":
            answer.append([r[1], "님이 나갔습니다."])
        elif r[0] == "Change":
            user[r[1]] = r[2]
    
    for i in range(len(answer)):
        if answer[i][0] in user.keys():
            answer[i] = user[answer[i][0]] + answer[i][1]
            
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))