def solution(prices):
    answer = []
    N = len(prices)
    for i in range(N):
        cnt = 0 
        for j in range(i+1, N):
            cnt+=1
            if prices[j] < prices[i] :
                break

        answer.append(cnt)

    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))