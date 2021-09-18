def isPalindrome(n):
    # 팰린드롬수인지 확인
    num = str(n)
    length = len(num)

    for i in range(length//2):
        if num[i] != num[length-i-1]:
            return False
    
    return True

while True:
    n = int(input())
    if n == 0:
        break

    if isPalindrome(n):
        print("yes")
    else:
        print("no")
        
