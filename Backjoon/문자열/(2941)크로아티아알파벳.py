word = input()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for a in alphabet:
    # replace 하면 값을 반영해야 함
    word = word.replace(a, "0") # 크로아티아 알파벳이면 한단어로 변환
print(len(word)) 