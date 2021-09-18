n = int(input())
# 중복 제거
words = list(set([input() for _ in range(n)]))

# 정렬 (다중 조건)
words.sort(key=lambda x: (len(x), x))

# 출력
for word in words:
    print(word)
