def solution(sticker):
    answer = 0
    # dp[i] : i번째 인덱스까지 최대 값
    # dp[i] = max(dp[i-1], dp[i-2] + sticker[i])   
    dp1 = [0 for _ in range(len(sticker))]
    dp2 = [0 for _ in range(len(sticker))]
    
    # 첫번째 스티커를 때는 경우 -> 마지막 스티커를 제외
    dp1[0] = sticker[0]
    if len(dp1) > 1:
        dp1[1] = dp1[0]
        
    for i in range(2, len(sticker)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    
    # 첫번째 스티커를 때지 않는 경우 -> 마지막 스티커까지 확인
    dp2[0] = 0
    if len(dp2) > 1:
        dp2[1] = sticker[1]
        
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])

    return max(max(dp1), max(dp2))