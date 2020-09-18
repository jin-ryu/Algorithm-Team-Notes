# 프로그래머스에서 5, 11 번 테스트케이스 안되는데, 내가 찾은 값이 최소인 것 같음

def solution(name):
    answer = 0
    name = list(name)
    name_board = list('A' * len(name))
    Ablocks, block = [], ""
    idx, end, n = 0, -1, 1   # 탐색 인덱스, (뒤에서 탐색 시) 탐색 종료 인덱스, 탐색 방향

    # A들이 모여있는 A 블록을 찾음
    for i in range(len(name)):
        if name[i] == "A":
            block += "A"
        elif block: 
            start = i - len(block) 
            Ablocks.append([block, start])  # [A 블록, 시작 인덱스] 
            block = ""

    if Ablocks:    
        max_Ablock = max(Ablocks)   # 가장 긴 A 블록을 찾음


    while name != name_board:
        # 뒤에서 탐색 시 A블록의 끝에 도달하면 종료
        if end != -1 and end == idx:
            answer -= 1
            break
        
        # Ablock이 없거나 max_Ablock에 아직 도달하지 않은 경우
        if not Ablocks or idx != max_Ablock[1]:
            abs_A = abs(ord(name[idx]) - ord("A")) 
            abs_Z = abs(ord(name[idx]) - ord("Z")) + 1
            answer += min(abs_A, abs_Z)

            name_board[idx] = name[idx]
            # 커서 이동   
            idx += 1 * n
            answer += 1     
   
        # max_Ablock의 시작 위치에 도달한 경우
        else:
            end =  idx + len(max_Ablock[0]) - 1     # 탐색 종료 시점
            if idx == 0:
                answer += 1
            idx = len(name) - 1     # 맨 끝으로 위치 이동
            n *= -1                 # 인덱스 뒤로 탐색하게 바꿈


    return answer - 1 

name = "JEROEN"
print(solution(name))   # 56  
name1 = "JAN"
print(solution(name1))  # 23
name2 = "JAZ"
print(solution(name2))  # 11

print(solution("BBBAAAB"))       # 9 (내가 볼 때는 7인데)
print(solution("ABABAAAAABA"))   # 11 (내가 볼 때는 8인데)
print(solution("CCAAC"))          # 8
print(solution("AAABAA"))         # 4
