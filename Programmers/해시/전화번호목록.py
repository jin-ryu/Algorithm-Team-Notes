# 인터넷 검색해서 힌트보고 해결
def solution(phone_book):
    answer = True
    phone_book.sort()    # 알파벳순(문자순)으로 정렬해놓을 경우 양옆만 비교하면 됨
    
    # zip으로 두개의 문자열을 비교하게 반복문을 짤 수 있음
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            answer = False
            break

    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))

phone_book1 = ["123","456","789"]
#print(solution(phone_book1))

phone_book2 = ["12","123","1235","567","88"]
#print(solution(phone_book2))
