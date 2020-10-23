import string
def solution(S):
    alphabets = []
    numbers = 0

    for ch in S:
        if ch in string.digits:
            numbers += int(ch)
        else:
            alphabets.append(ch)

    alphabets.sort()
    return "".join(alphabets) + str(numbers)
            


print(solution("K1KA5CB7")) # ABCKK13
print(solution("AJKDLSI412K4JSJ9D")) # ADDIJJJKKLSS20