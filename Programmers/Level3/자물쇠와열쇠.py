import numpy as np

def match(N, x, y, key, lock):
    board = [[0 for _ in range(N)] for _ in range(N)]
    start = len(key)-1      # lock 시작 인덱스
    end = start + len(lock)     # lock 끝 인덱스
    
    # key와 lock을 합침
    for i in range(N):
        for j in range(N):
            if x <= i < x+len(key) and y <= j < y+len(key):
                board[i][j] += key[i-x][j-y]
            
            if start <= i < end and start <= j < end :
                board[i][j] += lock[i-start][j-start]
                
    # key와 lock이 잘 맞는지 확인
    for i in range(start, end):
        for j in range(start, end):
            if board[i][j] != 1:
                return False
            
    return True
            
    
def solution(key, lock):
    # key와 lock 이 만나서 겹치는 곳 없이 lock에 1을 다 채워라!
    N =  len(lock) + 2 * (len(key) -1)
    
    for _ in range(4):
        key = list(map(list, np.rot90(key, k=-1)))   # 시계방향으로 회전
        for i in range(N):
            for j in range(N):
                #(i, j) : key의 시작 위치

                if match(N, i, j, key, lock):    # 하나라도 매치되는 경우가 있으면 True
                    return True
    
    return False