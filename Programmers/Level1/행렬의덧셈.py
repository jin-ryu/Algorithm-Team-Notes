def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    return arr1

# 좋은 예시   
def sumMatrix(A,B):
    # zip(*iterable): iterable의 요소들을 같은 index끼리 새로운 tuple로 만들어줌
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    
    # 동작 과정 확인해보기
    for a, b in zip(A, B):
        print(a, b)
        for c, d in zip(a, b):  
            print(c, d)
        
    return answer

# print(sumMatrix([[1,2],[2,3]], [[3,4],[5,6]]))  # [[4,6],[7,9]]
print(sumMatrix([[1],[2]], [[3],[4]]))  # [[4],[6]]