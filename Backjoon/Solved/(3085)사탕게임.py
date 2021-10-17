N = int(input())
board = [input() for _ in range(N)]

def check(N, board):
    max_value = 0
    
    for i in range(N):
        now = board[i][0]
        cnt = 0
        
        for j in range(N):
            if board[i][j] == now:
                cnt += 1
            else:
                max_value = max(max_value, cnt)
                cnt = 1
                now = board[i][j]

        max_value = max(max_value, cnt)
        
        
    for j in range(N):
        now = board[0][j]
        cnt = 0
        
        for i in range(N):
            if board[i][j] == now:
                cnt += 1
            else:
                max_value = max(max_value, cnt)
                cnt = 1
                now = board[i][j]

        max_value = max(max_value, cnt)


    return max_value

result = 0
board = list(map(list, board))

for i in range(N):
    for j in range(N-1):
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        result = max(result, check(N, board))
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        
for j in range(N):
    for i in range(N-1):
        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        result = max(result, check(N, board))
        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        

print(result)