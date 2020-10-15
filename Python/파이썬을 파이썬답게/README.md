# 파이썬을 파이썬답게



#### ■ Glossary

- **iterable** 
  -  자신의 맴버를 한번에 하나씩 리턴할 수 있는 객체
  - list, str, tuple, dict 등이 여기에 속함
- **sequence**
  - int 타입 인덱스를 통해, 원소에 접근할 수 있는 iterable (인덱싱이 가능)
  - list, str, tupe 등이 여기 속함 
  - dictionary는 다양한 타입을 통해 원소에 접근할 수 있기 때문에 sequence에 속하지 않음



#### ■ Practice

##### 01.divmod.py     몫과 나머지

- `divmod(a,b)` : a를 b로 나눈 몫과 나머지를 튜플로 반환

##### 02.changeBase.py     n진법으로 표기된 string을 10진법 숫자로 변환하기

- `int(x, base=10)` : base 진수인 x(숫자 아님)를 10진수 int로 변환
  ex) int('3212', 5) :  5진수 '3212'를 10진수로 변환

##### 03.sortStr.py     문자열 정렬하기

- `str.ljust(length)` : 좌측 정렬 (length는 전체 길이)
- `str.rjust(length)` : 우측 정렬 (length는 전체 길이)
- `str.center(length)` : 가운데 정렬 (length는 전체 길이)

##### 04.stringModule.py     알파벳 출력하기

- `import string`	
- `string.ascii_lowercase` : 알파벳 소문자 리스트
- `string.ascii_uppercase` : 알파벳 대문자 리스트
- `string.ascii_letters` : 알파벳 대소문자 리스트
- `string.digits` : 숫자 0~9 리스트

##### 05.sorted.py     원본을 유지한채, 정렬된 리스트 구하기

- `list.sort()` : 원본의 순서를 변경하여 정렬
- `sorted(list)` : 원본의 순서를 변경하지 않고 정렬 (새로운 리스트 생성)

##### 06.zip.py     2차원 리스트 뒤집기

- `zip(*iterables)` :  각 iterables의 요소들을 모으는 iterator를 만듭니다. tuple의 iterator를 돌려주는데, i 번째 튜플은 각 인자로 전달된 sequence나 iterable의 i 번째 요소를 포함합니다.
  (쉽게 말하면, 인자로 들어온 iterables의 요소들을 같은 index끼리 새로운 tuple로 만들어줌)

  - 사용 예#1 - 여러 개의 iterable 동시에 순회할 때 사용

    ```python
    list1 = [1, 2, 3, 4]
    list2 = [100, 120, 30, 300]
    list3 = [392, 2, 33, 1]
    answer = []
    for i, j, k in zip(list1, list2, list3):
       print( i + j + k )
    ```

  - 사용 예#2 - Key 리스트와 Value 리스트로 딕셔너리 생성하기

    ```python
    animals = ['cat', 'dog', 'lion']
    sounds = ['meow', 'woof', 'roar']
    
     # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
    answer = dict(zip(animals, sounds))
    ```

##### 07.map.py     모든 맴버의 type 변환하기

- `map(func, iterable)` : iterable의 모든 요소에 동일한 함수를 적용시킴

  ```python
  list1 = ['1', '100', '33']
  list2 = list(map(int, list1))
  ```

##### 08.mapAdvanced.py     map 함수 응용하기

- ` answer = list(map(len, mylist))`

##### 09.sequenceJoin     sequence 맴버를 하나로 이어 붙이기

- `str.join(list)` :  리스트에 있는 원소들을 (str을 기준으로) 합쳐서 문자열 생성
  -  `"".join(mylist)`는 공백 없이 리스트에 있는 원소들을  합쳐줌

##### 10.sequenceStar     삼각형 별찍기 - sequence type의 * 연산

- `str * n` : str이 n번 반복되는 새로운 문자열을 생성
- `list * n` : list의 원소들이 n반 반복되는 새로운 리스트 생성

##### 11. catesianProduct.py      곱집합(Cartesian product) 구하기

- 곱집합: 집합 A의 원소 a와 B의 원소 b로 만들어지는 순서쌍 (a, b)의 전체로 이루어진 집합
- `import itertools`
- `itertools.product(*iterables)` : iterables의 곱집합을 구함

##### 12.listSum.py      2차원 리스트를 1차원으로 만들기

- `sum(iterable, start)`  
  - Return the sum of a 'start' value (default: 0) plus an iterable of numbers
  - `sum([1,2,3])` : 1+2+3을 계산해 6을 리턴
  - `sum([[1,2], [3,4], [5,6]], [])` : [1,2] + [3,4] +[5,6]을 계산해 [1,2,3,4,5,6,]을 리턴
  - **제일 느림 사용하지 말 것**
- `itertools.chain.from_iterable(iterable)`
  - 하나의 iterable만 전달해도 iterator의 요소들을 조회하면서 값을 넘겨줌
- `itertools.chain(*iterables)`
  - 인자 앞에 *(Asterisk)을 붙여야 함
    - *(Asterisk) : 매개변수를 가변적인 개수를 가진 위치 인수로 정의
  - iterable한 컨테이너 데이터를 unpacking하여 전달
- list comprehension : for문을 한 줄로 동작하게 해줌
  - `[element for array in list for element in array]`
- `reduce(function, sequence[, initial])`
  - `import functools`
  - initial 값을 기준으로 데이터를 루프돌면서 functions을 계속해서 적용하여 데이터 누적
  - function에는 두 개의 인자 accumulator(누적자), current value(현재 값)가 필요
    - accumulator(누적자)  : 함수의 실행 시작부터 끝까지 계속해서 재사용되는 값
    - current value(현재 값) :  루프를 돌면서 계속 바뀌는 값
  - `lambda parameters : expression`
    - 함수를 딱 한 줄만으로 만들게 해줌
    - `lambda x,y : x+y`
  - `operator.add(x, y)`
    - `import operator`
- `numpy.array(list).flatten().tolist()`
  - `import numpy`
  - `flatten()` : 다차원 배열을 1차원으로 바꿔줌
    - 비슷한 함수 : `ravel()`, `reshape()`
    - **제일 빠름**

##### 13.combperm.py     순열과 조합

- `itertools.permutations(iterable, r=None)` : iterable의 r순열 계산
- `itertools.combinations(iterable, r)` : iterable의 r조합 계산

##### 14.alphabetCounter.py     가장 많이 등장하는 알파벳 찾기

- `counter = colletions.Counter(iterable)` 
  - `import collections`
  - 리스트의 요소와 개수를 딕셔너리 형태를 가진 Counter 객체로 반환 
    ex. Counter({'Tom' : 2, 'Tick' : 1})
  - dictionary를 확장하고 있기 때문에 dictionary에서 제공하는 API를 그대로 사용가능
  - `counter.update(iterable)` : 추가된 리스트를 누적해서 count
  - `counter.most_common(n)` : 가장 많이 나타난 요소 n개를 반환 
    (n 생락 시, 전체 리스트의 요소와 개수를 딕셔너리 형태로 반환)

##### 15.listComprehension.py     List comprehension의 if 문

- list comprehension을 사용하면 한 줄 안에 for문과 if문을 한번에 처리 할 수 있음
- [ ( 변수를 활용한 값 ) for ( 사용할 변수 이름 ) in ( 순회할 수 있는 값 )]

```python
mylist = [3,2,6,7]

answer = [i**2 for i in mylist if i%2==0] # 짝수인 경우 제곱한 값들의 리스트를 반환
```

##### 16.flagOrElse.py     for-else

- `math.squrt(n)` : 루트 n을 계산
  - `import math`
- **for - else **
  - else : for문이 중간에 break 등으로 끊기지 않고 끝까지 수행되었을 때 수행하는 코드

##### 17.swap.py     두 변수의 값 바꾸기

- `a, b = b, a` : a, b의 값을 교환

##### 18.binarySearch.py     이진 탐색하기 

- **이진탐색(Binary Search)**
  - **오름차순으로 정렬된 리스트**에서 특정한 값의 위치를 찾는 알고리즘
  - 한번 비교를 거칠 때 탐색 범위가 1/2로 줄음 
  - 검색 속도가 아주 빠름

- `bisect.bisect_left(a, x, lo=0, hi=len(a))`
  - 정렬된 순서를 유지하도록 a에서 x를 삽입할 위치를 찾음
  - x가 a에 이미 있으면, 삽입 위치는 기존 항목 앞(왼쪽)이 됨
  - `lo, hi=len(a)` : 고려해야할 리스트의 부분집합을 지정하는 데 사용
  - `bisect.bisect_left(mylist, 3)` : 리스트에서 3이 들어갈 위치 or 3의 위치를 반환
- `bisect.bisect_right(a, x, lo=0, hi=len(a))`
- `bisect.bisect(a, x, lo=0, hi=len(a))`
  - `bisect_left()` 와 비슷하지만, a에 있는 x의 기존 항목 뒤(오른쪽)에 오는 삽입 위치를 반환

##### 19.classInstance.py     클래스 인스턴스 출력하기

- `__str__`  : class 내부에서 출력 format을 지정할 수 있음

```python
class Coord(object):
    def __init__ (self, x, y):
        self.x, self.y = x, y
    def __str__ (self):
        return '({}, {})'.format(self.x, self.y)

point = Coord(1, 2)
```

##### 20.maxValue.py     가장 큰 수, inf

- `float('inf')` : float에서 가장 큰 수 (양수)
- `float('-inf')` : float에서 가장 작은 수  (음수)





---

*Reference: <https://programmers.co.kr/learn/courses/4008>*