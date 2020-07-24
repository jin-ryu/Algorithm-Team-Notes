import itertools

# 곱집합 Catesian product
# 'ABCD', 'xy' 의 곱집합
# Ax, Ay, Bx, By, Cx, Cy, Dx, Dy

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

result = list(itertools.product(iterable1, iterable2, iterable3))
print(result)
