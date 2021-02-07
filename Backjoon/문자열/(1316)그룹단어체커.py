n = int(input())
words = [input() for _ in range(n)]

def isGroupWord(word):
    used = []
    for i in range(len(word)):
        if word[i] not in used:
            # 처음 나온 알파벳이면 추가
            used.append(word[i])    
        elif i-1 >= 0 and word[i-1] != word[i]:
            # 사용된 알파벳인데 이전 알파벳과 다른 경우
            return False
    return True

count = 0
for word in words:
    if isGroupWord(word):
        count += 1
    
print(count)