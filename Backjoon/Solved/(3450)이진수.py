n = int(input())
T = [int(input()) for i in range(n)]

for t in T:
    binary = ""
    while t > 0:
        binary += str(t%2)
        t //= 2

    for i in range(len(binary)):
        if binary[i] == '1':
            print(i, end=" ")

