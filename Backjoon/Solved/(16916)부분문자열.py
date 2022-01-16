S = input()
P = input()

j = 0 
for i in range(len(S)):
    if S[i] == P[j]:
        if j >= len(P)-1:
            print(1)
            break
        j += 1
    else:
        j = 0   # 초기화
else:
    print(0)