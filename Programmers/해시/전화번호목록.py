def solution(phone_book):
    answer = True

    lens = list(map(len, phone_book))
    mins = [ph for ph in phone_book if len(ph) == min(lens)]
    
    for ph in phone_book:
        for m in mins:
            if ph.find(m):
                answer = False

    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))

