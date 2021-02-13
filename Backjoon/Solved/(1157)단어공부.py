from collections import Counter

arr = input().upper()
counter =  Counter(arr).most_common()
# 가장 많이 사용된 알파벳, 카운트
result = counter[0]
if len(counter) >= 2 and counter[1][1] == result[1]:
    # 가장 많이 사용된 알파벳이 여러개인 경우
    print("?")
else:
    print(result[0])
    
