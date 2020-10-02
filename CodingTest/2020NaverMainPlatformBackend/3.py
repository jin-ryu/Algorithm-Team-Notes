def solution(N):
    # write your code in Python 3.6
    flag = 0
    if N < 0:
        N = -N
        flag = 1
    
    mylist = [int(i) for i in str(N)]
    
    for i in range(len(mylist)):
        if flag == 0 and mylist[i] < 5:
            mylist.insert(i, 5)
            break
        if flag == 1 and mylist[i] > 5:
            mylist.insert(i, 5)
            break
    else:
        mylist.insert(len(mylist), 5)
        
    answer = int("".join(map(str, mylist)))
    if flag:
        answer = -answer
    
    return answer

print(solution(999))