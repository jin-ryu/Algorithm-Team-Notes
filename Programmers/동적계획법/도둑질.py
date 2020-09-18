# table[i]: i번째 집까지 털었을 때의 최댓값
# i가 3이상일때, table[i] = max(table[i-2]+table[i], table[i-1]) 
def solution(money):    
    table1 = [0]*len(money)
    table2 = [0]*len(money)

    # 첫번째 집을 터는 경우
    table1[0] = money[0] 
    table1[1] = max(money[1], table1[0])  
    for i in range(2, len(money)-1):   # 첫번째 집을 터는 경우 마지막 집은 털수 없음
        table1[i] = max(table1[i-2] + money[i], table1[i-1]) 

    # 마지막 집을 터는 경우
    table2[1] = money[1]    # 마지막 집을 터는 경우 첫번째 집은 털 수 없으므로 table2[0] = 0으로 둠
    for i in range(2, len(money)):
        table2[i] = max(table2[i-2] + money[i], table2[i-1]) 

    return max(max(table1), max(table2))
    

print(solution([1, 2, 3, 1]))    # 4
print(solution([10, 2, 2, 100, 100])) 
