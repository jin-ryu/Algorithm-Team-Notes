answer = 0

def find(board):
    # 제거할 2x2 블록을 찾는 함수
    blocks = set()
    for i in range(len(board)-1):
        for j in range(len(board[i])-1):
            if j >= len(board[i+1])-1:
                # 오른쪽 열의 높이가 현재 열의 높이보다 같거나 작은 경우 패스
                continue
            if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                # 2x2 블럭이면 좌표 추가
                for x, y in ((i, j), (i+1, j), (i, j+1), (i+1, j+1)):
                    blocks.add((x,y))
    
    return blocks

def delete(board, blocks):
    global answer
    
    # 높이순으로 정렬하고 내림차순
    for i, j in reversed(sorted(blocks)):
        # j번째 요소 삭제
        board[i].pop(j)
        answer += 1
        
    return board

def solution(m, n, board):
    # 블록의 방향을 반대로 바꿈 (열의 맨 밑부터 맨 위까지를 하나로)\
    board = [[board[i][j] for i in reversed(range(m))] for j in range(n)]
    
    while True:
        blocks = find(board)
        if not blocks:
            break
        # 보드 갱신
        board = delete(board, blocks)
    
    return answer

print(solution(6, 6, ["IIIIOO", "IIIOOO", "IIIOOI", "IOOIII", "OOOIII", "OOIIII"])) # 답: 32
answer = 0
print(solution(4,2, ["CC", "AA", "AA", "CC"]))  # 8
answer = 0
print(solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ'] ))# 15
