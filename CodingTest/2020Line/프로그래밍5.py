def solution(cards):
    answer = 0
    player = []     # player가 뽑은 카드 목록
    dealer = []     # dealer가 뽑은 카드 목록
    index = 4

    player.append(cards[0]) # 1
    fliped_card = cards[1]  # 2
    player.append(cards[2]) # 3
    show_card = cards[3]    # 4
    dealer.append(fliped_card)
    dealer.append()

    for _ in range(10000):  # 전체 카드 개수 만큼 반복(cards의 길이는 1 이상 10,000 이하)
        if sum_cards(player) == 21: # 블랙잭
            if sum_cards(dealer) != 21:
                answer += 3  
                break
        elif show_card == 1 or 7:
            while sum_card(player) >= 17:
                player.append(card[index])
                index += 1
            i    
        
    return answer

def sum_card(cards):
    sum = 0

    for card in cards:
        if card == 1:   # 1이면 일단 1만 더하고 스킵
            count += 1
            sum += 1
            continue

        if card == 11 or 12 or 13:
            sum += 10
        sum += card

    for _ in range(count):
        sum += 10
        if 17 <= sum <= 21: # 17~21 사이 숫자가 될 때까지 10을 더해줌
            break 

    return sum
            
print(solution([12, 7, 11, 6, 2, 12]))
"""
print(solution([1, 4, 10, 6, 9, 1, 8, 13]))
print(solution([10, 13, 10, 1, 2, 3, 4, 5, 6, 2]))
print(solution([3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))
"""