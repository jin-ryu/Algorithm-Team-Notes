# [부스트코스] 머신러닝을 위한 파이썬

⭐ **유찌니의 미래 투자 프로젝트 1**

- 파이썬으로 알고리즘을 하면서도 파이썬을 잘 모르는 것 같아서

- 언젠가는 머신러닝으로 멋진 프로젝트를 하기 위해서



## Pythonic Code

- 예시: 여러 단어들을 하나로 붙일 때

  ```python
  colors = ["red", "blue", "green", "yellow"]
  result = "".join(colors)
  ```

- 파이썬 스타일의 코딩 기법
- **파이썬 특유의 문법**을 활용하여 효율적으로 코드를 표현함
- 고급 코드를 작성할수록 더 많이 필요해짐

### Split & Join

- Split 함수
  - String Type의 값을 나눠서 List 형태로 변환

    ```python
    # 빈칸을 기준으로 문자열 나누기
    items = 'zero one two three'.split()	
    # ","을 기준으로 문자열 나누기
    example = 'python,jquery,javascript'.split(",")	
    # 리스트에 있는 각 값을 a,b,c 변수로 unpacking
    a, b, c= example.split(",")	
    # "."을 기준으로 문자열 나누기 -> unpacking
    example = 'cs50.gachon.edu'
    subdomain, domain, tld = example.split(".")
    ```

- Join 함수

  - String List를 합쳐 하나의 String으로 반환할 때 사용

    ```python
    colors = ["red", "blue", "green", "yellow"]
    result = ''.join(colors)
    result1 = ' '.join(colors)	# 연결 시 빈칸 1칸으로 연결
    result2 = ', '.join(colors) # 연결 시 ", "으로 연결
    result3 = '-'.join(colors) # 연결 시 "-"으로 연결
    ```

### List Comprehension

- 기존 List를 사용하여 간단히 다른 List를 만드는 기법

- 포괄적인 List, 포함되는 리스트라는 의미로 사용됨

- 파이썬에서 가장 많이 사용되는 기법 중 하나

- 일반적으로 for + append 보다 속도가 빠름

- List Comprehenstion

  ```python
  # 0~10의 정수 리스트
  result = [i for i in range(10)]
  # 0~10의 짝수 리스트 (필터)
  result = [i for i in range(10) if i % 2 == 0]
  ```

- Nested For loop

  ```python
  word_1 = "Hello"
  word_2 = "World"
  # one dimensional list
  result = [i+j for i in word_1 for j in word_2]
  # Result: ['HW', 'Ho', "Hr", "Hl", ...]
  ```

- Nested For loop + if 문

  ```python
  case_1 = ["A", "B", "C"]
  case_2 = ["D", "E", "A"]
  result = [i+j for i in case_1 for j in case_2]
  
  # Filter: i랑 j가 같다면 List에 추가하지 않음
  result = [i+j for i in case_1 for j in case_2 if not(i==j)]
  result.sort()
  ```

- split + list Comprehension

  ```python
  # 문장을 빈칸 기준으로 나눠 list로 반환
  words = 'The quick brown fox jumps over the lazy dog'.split()
  
  # list의 각 elements들을 대문자, 소문자, 길이로 변환하여
  # two dimensional list로 변환
  stuff = [[w.upper(), w.lower(), len(w)] for w in words]
  
  for i in stuff:
      print(i)
  ```

### Enumerate & Zip

- Enumerate

  - List의 element를 추출할 때 번호를 붙여서 추출

  - for + enumerate

    ```python
    for i, v in enumerate(['tic', 'tac', 'toe']):
        # list에 있는 index와 값을 unpacking
        print(i, v)
    ```

  - enumerate + list

    ```python
    mylist = ["a", "b", "c", "d"]
    # list의 index와 값을 unpacking하여 list로 저장
    mylist = list(enumerate(mylist))
    ```

  - enumerate + dictionary

    ```python
    # 문장을 list로 만들고 list의 index와 값을 unpacking하여 dict로 저장
    dict = {i:j for i, j in enumerate('Gachon University is an academic institute located in Soute Korea'.split())}
    # {0:"Gachon" 1:"University", 2:"is", ...}
    ```

- Zip

  - 두 개의 list의 값을 병렬적으로 추출함

  - for loop + zip

    ```python
    alist = ['a1', 'a2', 'a3']
    blist = ['b1', 'b2', 'b3']
    # 병렬적으로 값을 추출
    for a, b in zip(alist, blist):
        print(a, b)	
    ```

  - list comprehension + zip

    ```python
    # 각 tuple의 같은 index끼리 묶음
    a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
    print(a, b, c)
    # vector 연산 등에서 자주 사용
    print([sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))])
    ```

  - enumerate + zip

    ```python
    alist = ['a1', 'a2', 'a3']
    blist = ['b1', 'b2', 'b3']
    
    for i, (a, b) in enumerate(zip(alist, blist)):
        print(i, a, b)	# index alist[index] blist[index] 표시
    ```

### Lambda & MapReduce

- Lambda

  - 함수 이름 없이, 함수처럼 쓸 수 있는 익명 함수

  - 수학의 람다 대수에서 유래함

  - Python 3부터는 권장하지는 않으나 여전히 많이 쓰임

    - 이유: list comprehension으로 대부분 처리 가능함

    ```python
    f = lambda x, y: x + y
    print(f(1, 4))
    
    f = lambda x: x ** 2
    print(f(3))
    
    f = lambda x: x / 2
    print(f(3))
    
    print((lambda x: x + 1)(5))
    ```

- Map function

  - Sequence 자료형 각 element에 동일한 functions을 적용함

    ```python
    ex = [1, 2, 3, 4, 5]
    f = lambda x: x ** 2
    print(list(map(f, ex)))
    
    ex = [1, 2, 3, 4, 5]
    f = lambda x, y: x + y
    print(list(map(f, ex, ex)))
    
    # lambda function filter
    list(map(
        lambda x: x ** 2 if x % 2 == 0 else x,
        ex))
    
    # python 3에는 list를 꼭 붙여줘야함
    ex = [1,2,3,4,5]
    print(list(map(lambda x: x+x, ex)))
    print((map(lambda x: x+x, ex)))	# map 객체가 반환됨
    
    f = lambda x: x ** 2
    print(map(f, ex))
    for i in map(f, ex):
        print(i)
    
    result = map(f, ex)
    print(result)
    print(next(result))
    
    import sys
    sys.getsizeof(ex)
    sys.getsizeof((map(lambda x: x+x, ex)))
    sys.getsizeof(list(map(lambda x: x+x, ex)))
    ```

- Reduce Function

  - map function과 달리 list에 똑같은 함수를 적용해서 통합

    ```python
    # Reduce
    from functools import reduce
    print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))	# 15(=1+2+3+4+5)
    
    def factorial(n):
        return reduce(
                lambda x, y: x*y, range(1, n+1))
    
    factorial(5)	# 12-(1x2x3x4x5)
    ```

- Summary
  - Lambda, map, reduce는 간단한 코드로 다양한 기능을 제공
  - 그러나 코드의 직관성이 떨어져서 lambda나 reduce는 **python3에서 사용을 권장하지 않음**
  - Legacy library나 다양한 머신러닝 코드에서 여전히 사용중

### Asterisk

- 흔히 알고 있는 *를 의미함

- 단순 곱셈, 가변 인자 활용 등 다양한 것이 사용됨

- *args 

  ```python
  def asterisk_test(a, *args):	# 1 (2,3,4,5,6)
      print(a, args)	# tuple 타입
      print(type(args))
  
  asterisk_test(1,2,3,4,5,6)
  ```

- **kargs 

  ```python
  def asterisk_test(a, **kargs):	# 1 {'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
      print(a, kargs)	# dictionary 타입
      print(type(kargs))
  
  asterisk_test(1, b=2, c=3, d=4, e=5, f=6)
  ```

- Asterisk - unpacking a container

  - tuple, dict 등 자료형에 들어가 있는 값을 unpacking (*)
  - 함수의 입력 값, zip 등에 유용하게 사용

  ```python
  a, b, c = ([1, 2], [3, 4], [5, 6])
  print(a, b, c)
  
  data = ([1, 2], [3, 4], [5, 6])
  print(*data)
  ```

  ```python
  for data in zip(*([1, 2], [3, 4], [5, 6])):
      print(sum(data))	# 원소 하나씩 탐색
  
  def asterisk_test(a, b, c, d, e=0):
      print(a, b, c, d, e)
  ```

  ```python
  data = {"d":1 , "c":2, "b":3, "e":56}
  asterisk_test(10, **data)	# dict unpacking
  ```

### <참고> Data Structure - Collections

- Collections

  - List, Tuple, Dict에 대한 Python Built-in 확장 자료 구조(모듈)

  - 편의성, 실행 효율 등을 사용자에게 제공함

  - 아래의 모듈이 존재함

    ```python
    from collections import deque
    from collections import Counter
    from collections import OrderedDict
    from collections import defaultedict
    from collections import namedtuple
    ```

- deque
  - Stack과 Queue를 지원하는 모듈
  - List에 비해 효율적인 자료 저장 방식을 지원함
  - rotate, reverse 등 Linked List의 특성을 지원함
  - 기존 list 형태의 함수를 모두 지원함
  - deque는 기존 list보다 효율적인 자료구조를 제공
  - 효율적 메모리 구조로 처리 속도 향상
- OrderedDict
  - Dict와 달리, 데이터를 입력한 순서대로 dict를 반환함
  - Dict type의 값을 value 또는 key 값으로 정렬할 때 사용 가능
- defaultDict
  - Dict type의 값에 기본 값을 지정, 신규값 생성시 사용하는 방법

- Counter
  - Sequence type의 data element들의 갯수를 dict 형태로 반환
- namedtuple
  - Tuple 형태로 Data 구조체를 저장하는 방법
  - 저장되는 data의 variable을 사전에 지정해서 저장함