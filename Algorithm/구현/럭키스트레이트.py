score = input()

N = len(score)
front, back = 0, 0

for i in range(N):
    if i < N//2:
        front += int(score[i])
    else:
        back += int(score[i])

if front == back:
    print("LUCKY")
else:
    print("READY")
