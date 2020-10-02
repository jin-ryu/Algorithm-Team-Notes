import bisect

# 이진 탐색(Binary Search)
# 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘
# 한번 비교를 거칠때 탐색 범위가 1/2로 줄음
# 검색 속도가 아주 빠름
mylist = [1, 2, 3, 7, 9, 11, 33]
print('index :', bisect.bisect_left(mylist, 3))