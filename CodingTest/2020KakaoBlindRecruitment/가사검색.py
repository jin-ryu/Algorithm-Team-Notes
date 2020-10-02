import re

def solution(words, queries):
    answer = []

    for query in queries:
        N = len(query) # query를 변경하기 전에 길이 저장
        count = query.count("?")  # "?"가 반복되는 횟수

        # Regex multiple repeat error를 방지하기 위해 query 수정
        if query[0] == "?":   # ?가 접두사로 주어지는 경우
            query = query[count:]   
            query = "[a-z]{" + str(count) + "}" + query     # 쿼리 앞에 붙이기

        elif query[-1] == "?":   # ?가 접미사로 주어지는 경우
            query = query[:-count]
            query = query + "[a-z]{" + str(count) + "}"     # 쿼리 뒤에 붙이기

        pattern = re.compile(query)
        count = 0
        for word in words:
            m = pattern.match(word)
            if N == len(word) and m :   # 정규식에 매치된다면 개수 증가
                count += 1
        answer.append(count)

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]))
# [3, 2, 4, 1, 0]