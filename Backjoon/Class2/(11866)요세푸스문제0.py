n, k = map(int, input().split())
people = [i for i in range(1, n+1)]
answer = []

idx = 0
for i in range(n):
    # 인덱스 갱신
    idx = (idx + k-1)%len(people)
    # 출력 용이하게 str 형태로 변환
    answer.append(str(people[idx]))
    people.pop(idx)

print("<" + ", ".join(answer) + ">")
