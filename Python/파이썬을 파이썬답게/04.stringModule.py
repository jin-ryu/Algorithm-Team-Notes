import string
# string.ascii_lowercase    알파벳 소문자
# string.ascii_uppercase    알파벳 대문자
# string.ascii_letters      알파벳 대소문자
# string.digits             숫자 0~9

num = int(input().strip())
if num == 0:
    for i in list(string.ascii_lowercase):
        print(i, end='')

else:
    for i in list(string.ascii_uppercase):
        print(i, end='')
        