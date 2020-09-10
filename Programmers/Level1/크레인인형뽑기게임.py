def solution(board, moves):
    answer = 0
    box = []

    # 스택 형태로 이차원 배열 변환
    stacks = list(map(list, zip(*board)))
    for i in range(len(stacks)):
        stacks[i].reverse()
        for j in range(len(stacks[i])-1, 0, -1):
            if stacks[i][j] == 0:
                del stacks[i][j]
            else:
                break
            
    # move 배열 값에 따라 인형 이동
    for move in moves:
        # 해당 라인에 인형이 없으면 스킵, 있으면 인형 삽입
        if stacks[move-1]:  
            box.append(stacks[move-1].pop())
            if len(box) >= 2 and box[-1] == box[-2]:
                box.pop()
                box.pop()
                answer += 2

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))

