import sys

t = int(sys.stdin.readline())
for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    # 1층부터 시작하고, 1번방부터 시작하기 때문에
    # 1씩 빼주고 나중에 더해줌
    floor = (n-1) % h + 1
    number = (n-1) // h + 1
    
    room = str(floor)
    if number < 10:
        # number가 한자리 숫자인 경우 앞에 0붙임 
        room += "0" + str(number)
    else:
        room += str(number)

    print(room)