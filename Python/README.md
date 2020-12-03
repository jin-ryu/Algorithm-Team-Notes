# Python Introduction
**💁 유찌니의 파이썬 노트**
##### Python 3.7 공식 문서: https://docs.python.org/3.7/

- [Number (숫자 자료형)](#number)
- [List (리스트)](#list)
- [String (문자열)](#string)
- [Tuple (튜플)](#tuple)
- [Dictionary (사전)](#dictionary)
- [Set (집합)](#set)
- [Input and Output (입출력)](#input-and-output)
- [Function (함수)](#function)
  - [Lambda](#lambda)
  - [Zip](#zip)
- [Conditional (조건문)](#conditional)
- [Libraries (표준 라이브러리)](#libraries)
- [진수 변환](#진수-변환)



##  Number 

- **지수 표현 방식**
  
  - e나 E 다음에 오는 수는 10의 지수부를 의미
  - 유효숫자e<sup>(지수)</sup> =  유효숫자*10<sup>(지수)</sup>
    - `1e9`: 10의 9제곱 (1,000,000,000)
  - 최단 경로 알고리즘에서는 도달할 수 없는 노드에 대하여 최단 거리를 **무한(INF)**로 설정
- 이때 가능한  최댓값이 10억 미만이라면 무한(INF)의 값으로 1e9를 이용할 수 있음
  
- **실수형 더 알아보기**

  - 오늘날 가장 널리 쓰이는 IEEE754 표준에서는 실수형을 저장하기 위해 4바이트, 혹은 8 바이트의 **고정된 크기**의 메모리를 할당하므로, **컴퓨터 시스템은 실수 정보를 표현하는 정확도에 한계를 가짐**
  - 실수 값을 비교할 때는 `round()` 함수 사용
    - `round(123.456, 2)` : 123.456을 소수 셋째자리에서 반올림

  ```python
  a = 0.3 + 0.6
  print(a)	# 0.899999999999 (2진수에서는 0.9를 정확히 표현할 수 없음)
  
  if a == 0.9:
      print(True)
  else:
      print(False)	# False가 나옴
      
  print(round(a, 4))	# 0.9
  
  if (round(a, 4)) == 0.9:
      print(True)		# True가 나옴
  else:
      print(False)	
  ```



##  List

- **List Comprehension**

  - 리스트를 초기화하는 방법 중 하나
    - `array = [i for i in range(10)]`
    - `array = [i for i in range(20) if i%2 == 1]`
    - `array = [i*i for i in range(10)]`
  - **2차원 리스트를 초기화**할때 효과적으로 사용될 수 있음
    - 특히 NxM 크기의 2차원 리스트를 초기화할때 매우 유용
      - **좋은 예시 **: `array = [[0] * for _ in range(n)]`	
      - **잘못된 예시 **: `array = [[0] * m] * n`
        - 위 코드는  전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식됨

- **리스트에서 특정 값을 가지는 원소를 모두 제거하기**

  ```python
  a = [1,2,3,4,5,5,5]
  remove_set = {3,5}	# 집합 자료형 - 특정한 값의 존재유무만을 판단할 때 유용 
  
  # remove_set에 포함되지 않은 값만을 저장
  result = [i for i in a if i not in remove_set]
  print(result)	# [1,2,4]
  ```

- **Methods**

  - `list1.append(value)` : 리스트에 새로운 값이 추가 

    - O(1) 시간

  - `list1.extend([value1, value2, ...])` : 리스트 뒤에 값을 추가

    - list1 = ['a', 'b', 'c', 'd']
      list1.append('ef')			# list2 = ['a', 'b', 'c', 'd', 'ef']
      list1.extend('ef')			 # list2 = ['a', 'b', 'c', 'd', 'e' ,'f']

  - `list1.index(value)` : 값을 이용하여 위치를 찾는 기능

  - `list1.insert(index, value)` : 원하는 위치에 값을 추가

  - `list1.remove(value)` : 특정 값을 지움
    (여러개의 값이 있는 경우 가장 앞에 있는 하나만 지워짐)

  - `list1.pop(index)`: index에 있는 값을 뽑음 (index 생략 시 가장 마지막 값을 뽑음)
    
  - `list1.count(value)` : 해당 값을 개수를 셈 

  - `list1.reverse()` : 리스트에 들어있는 요소들의 순서를 거꾸로 뒤집어줌

  - `list1.sort()` : 값을 순서대로 정렬 (list1의 원래값이 변함)

    - O(NlogN) 시간

    - `list1.sort(key = func)` : 값을 key 조건에 따라 정렬 

      - func 예시 : lambda x : x*3, len

      - 비교할 아이템의 요소가 복수 개일 경우, **튜플로 그 순서를 내보내주면 된다.**

        `sorted(e, key = lambda x : (x[0], -x[1]))`

    - `list1.sort(reverse = True)` : 값을 역순으로 정렬 (list1의 원래값이 변함)

  - `list2 = sorted(list1)` : 값을 순서대로 정렬 (list1의 원래값이 변하지 않음)

  - `if value in list1` : 리스트 안에 값이 들어있는지 확인 

  - `if valie not in list1` : 리스트 안에 값이 들어있지 않은 지 확인 

  - `del list1[index]` : 특정 위치의 값을 지움

  - `enumerate(list1)` : index와 value를 tuple 형태로 반환

    - 반복문 사용 시 몇 번째 반복문인지 확인할 필요가 있을 때 사용
    - 자주 사용하는 방식: `for index, value in enumerate(list1):`

  - `list(set(value))` : 중복되는 value를 제거

  - `ch.isupper()`: 문자가 대문자인지 확인

  - `ch.islower()`: 문자가 소문자인지 확인

- **Sort and Reverse**

  - `list.sort()`나 `list.reverese()`는 리스트라는 자료형에 한정된 메소드
    - 따라서 다른 자료형에서는 안될 수도 있다
  - `sorted()`나 `reversed()`는 괄호 안에 다양한 자료형을 지원한다
    - 따라서 자료형이 헷갈릴 경우는 이것을 사용하는 것이 좋을 것 같다

- **List and String**

  - 서로 변환이 가능하다
  - `list1 = str.split(' ')` : 문자열에서 리스트로 (' ' 단위로 분할)
  - `" ".join(list)` : 리스트에서 문자열로 (" "단위로 이어붙임)

- **Slice**

  - slice를 하면 해당하는 부분의 리스트나 문자열을 새로 만들어준다
  - String에서도 slice를 사용할 수 있다
  - `list1[start:end]` : 리스트의 start부터 end-1까지를 반환
  - `list1[start : end : step]` :  slice한 값의 범위에서 step 값을 주어 그 값만큼 건너뛰어 가져오는 기능
  - `del list1[ : end]` :  처음부터 end-1번째까지 삭제
  - `list1[1:3] = [77,88]` (더 많은/적은 개수로 변환도 가능)

- **리스트 간의 차집합은 list comprehension으로 구현**

  - [x **for** x **in** a **if** x **not** **in** b]

## String

- **문자열 안에 큰따옴표나 작은따옴표가 포함되어야 하는 경우**

  - 백슬래시(\\)를 사용하면, 큰따옴표나 작은따옴표를 원하는 만큼 포함시킬 수 있음

- **문자열 연산**

  - 덧셈(+) : 문자열이 더해져서 연결(Concatenate)
  - 곱셉(*) : 양의 정수와 곱하는 경우, 문자열이 그 값만큼 여러번 더해짐
  - 문자열에 대해서도 마찬가지로 인덱싱과 슬라이싱을 이용할 수 있음
    - **다만, 문자열은 특정 인덱스의 값을 변경할 수 없음(Immutable)**

- **Methods**

  - `string.split(str)` :  str 기준으로 문자열을 분리하여 리스트를 생성
  - `format()` : 포맷팅을 수행 / 중괄호 {}를 이용해 값을 대입
    - `print('My name is {} and I'm {} years old.format(Jin, 24))`
  - `end` : print() 함수에서 출력의 끝을 지정
    - `print('Python Introduction' , end='')`
  - `str.find(sub)`: str안에 sub가 서브스트링에서 존재하면 sub의 시작 위치를 반환, sub가 없다면 -1을 리턴 
  - `str1.startswith(str2)` : str2가 str1의 맨 앞에 있는지 여부를 True, False로 반환
  - `str1.endsswith(str2)` : str2가 str1의 맨 앞에 있는지 여부를 True, False로 반환
  - `ord(ch)`: 문자의 ASCII 코드를 리턴
  - `chr(num)`: ASCII 코드를 문자로 리턴
  - `s.isalpha()`: 문자열이 문자인지 아닌지 리턴
  - `s.isdigit()`: 문자열이 숫자인지 아닌지 리턴
  - `s.replace(sub, change, [count])`: 부분 문자열을 찾아 바꿔줌 (count는 선택항목)
    - s에 바로 반영되는 것이 아니므로  s=s.replace() 이런 형태로 사용해야 한다
  - `s.lower()`: 대문자를 소문자로 변환
  - `s.upper()`: 소문자를 대문자로 변환
  - `s.capitalize()`:  문자열의 첫 문자를 대문자로 변환
  
  

## Tuple

- 한번 선언된 값을 **변경, 삭제가 불가능**

- 리스트에 비해 상대적으로 공간 효율적임

- **튜플을 사용하면 좋은 경우**

  - **서로 다른 성질**의 데이터를 묶어서 관리해야 할 때
    - 최단 경로 알고리즘에서는 (비용, 노드 번호)의 형태로 튜플 자료형을 자주 사용
  - 데이터의 나열을 **해싱(Hashing)의 키 값**으로 사용해야 할 때
    - 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있음
  - 리스트보다 **메모리를 효율적으로** 사용해야 할 때

- **Methods**

  - `in` / `not in` 

- **Packing, Unpacking**

  - packing : 하나의 변수에 여러개의 값을 넣는 것
  - unpacking : 패킹된 변수에서 여러개의 값을 꺼내오는 것

  ```python
  c = (3,4)
  d,e = c			# c의 값을 unpacking하여 d,e에 값을 넣음
  f = d,e			# 변수 d와 e의 값을 f에 packing
  ```

- **Uses**

  - 두 변수의 값을 바꿀 때 임시 변수가 필요 없다 

    ```python
    a,b = b,a
    ```

  - 함수의 리턴 값으로 여러 값을 전달할 수 있다

    - **튜플 리스트 활용**	

      ```python
      for a in enumerate(list1):
          # 아래 두 문장은 같은 결과
          print('{}번째 값: {}'.format(a[0], a[1]))
      	print('{}번째 값: {}'.format(*a))
      ```

    - **튜플 딕셔너리 활용**

      ```python
      for a in dict.items():
          # 아래 두 문장은 같은 결과
          print('{}의 나이는:{}'.format(a[0], a[1]))
          print('{}의 나이는:{}'.format(*a))
      ```



## Dictionary

- 키(Key)와 값(Value)의 쌍을 데이터로 가지는 자료형
  
- 변경 불가능한(Immutable) 자료형을 키로 사용할 수 있음
  
- 해시 테이블(Hash Table)을 이용하므로 데이터의 조회 및 수정을 O(1)시간에 처
  
- **Methods**
  
  - `del(dict['one'])`  /`dict.pop('two')` : key 값에 따른 삭제
    
  - `dict.keys()` : key 값들을 dict_keys 객체의 형태로 반환 (리스트로 반환X)
    
  - `dict.values()` : value 값들을 dict_values 객체의 형태로 반환 (리스트로 반환X)
    
    - `dict.items()` : key, value 값들을 dict_items 객체의 형태로 반환 (리스트로 반환X)
      
      * 자주 사용하는 방식: `for key, value in dict.items():`
    
  - `dict['key']` : 해당 키 값에 해당하는 value 값 조회(에러 O)
    
  - `dict.get('key')` : 해당 키 값에 해당하는 value 값 조회(에러 X)
    
  - `dict['key'] = value` : 변수 내 키 + value 값 추가 
    
    - 'key' 값의 존재 여부 판단 방법
      - get 
        - `dict.get('key')`
        - value 값을 리턴하고 싶을 때는 get 사용 
      - in: 
        - `'key' in dict`
        - 키 값이 있는지만 확인하고 싶을 때 in 사용
    
  - max, min 활용법
    
    - key나 value 중에서 최대, 최소 구하기
    
      - `max(dict.values())` / `max(dict.keys())`
    
    - value 값이 최대인 key 구하기
    
    ```python
          def f1(key):
              return dict[key]
          
          key_max = max(dict.keys(), key=f1)
    ```        
        - `key_max = max(dict.keys(), key=(lambda k: dict[k])`
    
    
  - **List vs. Dictionary**
    <p align="center"><img src="https://user-images.githubusercontent.com/45402031/88435926-2f97e780-ce3e-11ea-8e1d-8d6ce975b1e0.png" width="50%"></p>
  
  

## Set

- **중복을 허용하지 않고, 순서가 없음**
- **초기화** : set() or set([1,2,3]) or set('123') or ({1,2,3})
- 데이터가 존재하는지 여부를 판단할때 자주 사용
- 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있음
- **Methods**
  - **집합 연산**
    - `a | b` : 합집합 (a에 속하거나 b에 속하는 원소로 이루어진 집합)
      - `a.union(b)`와 동일
    - `a & b` : 교집합 (a에도 속하고 b에도 속하는 원소로 이루어진 집합)
      - `a.intersection(b)`와 동일
    - `a - b` : 차집합 (a의 원소 중에서 b에 속하지 않는 원소로 이루어진 집합)
      - `a.difference(b)`와 동일
    - `a^b` : 대칭 차집합(합집합 - 교집합)  
      - `a.symmetric_difference(b)`와 동일
  - `k.add(item)`: 집합에 하나의 원소를 추가할 때 사용
  - `k.update([3, 4, 5])`: 집합에 여러개의 원소를 추가할 때 사용
  - `k.remove(item)` : 집합 원소를 제거할 때 사용 (해당 원소가 없으면 KeyError 발생)
  - `k.discard(item)`: 집합 원소를 제거할 때 사용 (해당 원소가 없어도 에러 발생하지 않음) 
  - **기타 메소드**
    - `a.issubset(b)` : 부분집합 여부 확인
    - `a.issuperset(b)` : issubset과 반대. superset인지 확인
    - `a.isdisjoint(b)` : 교집합이 없으면 True, 있으면 False



## Input and Output

- **표준 입력 방법**

  - `input()` : 한 줄의 문자열을 입력받는 함수

  - `map()` : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

  - **공백을 기준으로 구분된 데이터를 입력받을 때**

    - `list(map(int, input().split()))`
    - `a,b,c = map(int, input().split())` : 데이터의 개수가 많지 않은 경우 

  - **빠르게 입력 받기**

    ````python
    import sys
    
    data = sys.stdin.readline().rstrip()	# 문자열 입력 받기
    ````

    - 단, 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용
    - 이진탐색, 그래프, 정렬 등에서 활용될 수 있음

- **표준 출력 방법**

  - `print()`  

    - 각 변수를 콤마(,)를 이용하여 띄어쓰기로 구분하여 출력할 수 있음
    - 기본적으로 출력 이후에 줄 바꿈을 수행 
    - `print(value, end = " ")` : end 속성 이용하면 줄 바꿈 없앨 수 있음

  - **f-string**

    - 파이썬 3.6부터 사용가능하며, **문자열 앞에 접두사 'f'를 붙여 사용**
    - 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있음

    ```python
    answer = 7
    print(f"정답은 {answer}입니다.")
    ```



## Function

- **파라미터 지정하기** 

  ```python
  def add(a, b):
      return a+b
  
  add(b=3, a=7)	# 이 경우 매개변수의 순서가 달라도 상관이 없음
  ```

- **global 키워드**

  - global 키워드로 변수를 지정하면 해당 함수에는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조

  ```python
  a = 0	# 전역 변수
  
  def func():
      global a
      a += 1
      
  for i in range(10):
      func()
  
  print(a)	# 10
  ```

- **여러 개의 반환 값 (Packing/Unpacking)**

  ```python
  def operator(a,b):
      add_var = a+b
      subtract_var = a-b
      multiply_var = a*b
      divide_var = a/b
      
      return add_var, subtract_var, multiply_var, divide_var
  
  a, b, c, d = operator(7, 3)
  print(a, b, c, d)
  ```



### Lambda

- 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징
- `lambda (매개변수) : (반환값)`
- 함수 자체를 입력 매개 변수로 받는 경우 효과적으로 사용

- **기본적 활용**

  - `lambda x: int(x)` : 문자열 변수를 정수형으로 변환
  - `lambda x,y: x>y` : x, y 값을 비교
  - `lambda x: x[key]` : 딕셔너리에서 key를 이용해 value를 얻음

- **다른 내장 함수와의 활용**

  - **min, max** : custom key를 설정할 수 있음

  ```python
  # min, max 함수
  names = ['Suh', 'Adrian', 'Bill', 'Jonathan']
  
  # longest : 길이가 가장 긴 이름
  longest = max(names, key= lambda n: len(n))
  
  print(longest)
  ```

  - **sort, filter, map** : 함수에 조건을 설정할 수 있음

  ```python
  keys = [{'key': 8}, {'key': 5}, {'key': 9}, {'key': 3}]
  
  # sort 함수 - 정렬 키 조건 설정
  keys.sort(key = lambda x: x['key'])
  
  # filter 함수 - 필터 키 조건 설정
  filter(lambda x: x['key']<5, keys)
  
  # map 함수 - 여러개의 리스트에 동일한 프로세스 적용
  map(lambda x: x['key']+5, keys)
  ```




#### Zip

- `zip(*iterable)` :  iterables의 요소들을 같은 index끼리 새로운 tuple로 만들어줌

- 활용 방법

  - 여러 개의 iterable 동시 순회

    ```python
    list1 = [1, 2, 3, 4]
    list2 = [100, 120, 30, 300]
    list3 = [392, 2, 33, 1] 
    
    for i, j, k in zip(list1, list2, list3):
        # i = 1, 2, 3, 4
        # j = 100, 120, 30, 300
        # k =  392, 2, 33, 1
        print( i + j + k )	# 493, 124, 66, 305
    ```

  - key와 value 리스트로 딕셔너리 생성

    ```python
    animals = ['cat', 'dog', 'lion']
    sounds = ['meow', 'woof', 'roar']
    
     # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
    answer = dict(zip(animals, sounds))
    ```

  - 문자 하나씩 비교하기

    ```python
    a = "hit"
    b = "hot"
    
    cmp = zip(a,b)
    next(cmp) # ('h', 'h')
    next(cmp) # ('i', 'o')
    next(cmp) # ('t', 't')
    
    for x, y in cmp:
        if x != y:
            print("다르다")
        else:
            print("같다")
    ```




## Conditional

- **Methods**

  - `in` / `not in`

    - 리스트, 튜플, 문자열, 딕셔너리 모두에서 사용 가능

  - `pass`

    - 아무것도 처리하고 싶지 않을 때 pass 키워드 사용

      <small> ex) 디버깅 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분을 비워놓고 싶은 경우 </small>

- **조건문의 간소화**

  - 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있음

    ```python
    score = 85
    
    if score >= 80: result = "Success"
    else: result = "Fail"
    ```

  - 조건부 표현식(Conditional Expression)은 **if ~else문을 한 줄에 작성**할 수 있게 해줌

    ```python
    score = 85
    result = "Success" if score >= 80 else "Fail"	# if가 중간에 들어가는 것 주의
    ```

- **파이썬 조건문 내에서의 부등식**
  
  - 조건문 내에서 수학의 부등식을 그대로 사용할 수 있음 <small>ex) `x> 0 and x<20` -> `0<x<20`</small>




## Libraries

- **내장 함수**: 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들을 제공

  - `sum()`, `min()`, `max()`, `eval()`, `sorted()` 등
    - `eval(expression)`: expression을 계산해 반환 ex) `eval("(3+5)*7")`

- `itertools`: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공

  - 특히 순열과 조합 라이브러리는 코딩 테스트에서 자주 사용

  - **순열**: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것

    - {'A', 'B', 'C'}에서 세개를 선택하여 나열하는 경우: 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'

    ```python
    from itertools import permutations
    
    data = ['A', 'B', 'C']	# 데이터 준비
    
    result = list(permutations(data, 3))	# 모든 순열 구하기
    print(result) 	# ('A','B','C'), ('A','C','B'), ('B','A','C'), ('B','C','A'), ('C','A','B'), ('C','B', 'A')
    ```

  - **조합**: 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것

    - {'A', 'B', 'C'}에서 순서를 고려하지 않고 두개를 뽑는 경우 : 'AB', 'AC', 'BC'

    ```python
    from itertools import combinations
    
    data = ['A', 'B', 'C']	# 데이터 준비
    
    result = list(combinations(data, 2))	# 모든 순열 구하기
    print(result) 	# ('A','B'), ('A','C'), ('B','C')
    ```

  - **중복 순열**

    ```python
    from itertools import product 
    
    data = ['A', 'B', 'C']	# 데이터 준비
    
    result = list(product(data, repeat=2))	# 2개를 뽑는 모든 순열 구하기 (중복 허용)
    print(result) 	
    ```

  - **중복 조합**

    ```python
    from itertools import combinations_with_replacement
    
    data = ['A', 'B', 'C']	# 데이터 준비
    
    result = list(combinations_with_replacement(data, 2))	# 2개를 뽑는 모든 조합 구하기 (중복 허용)
    print(result) 	
    ```

- `heapq`: 힙(Heap) 자료구조를 제공

  - 일반적으로 우선순위 큐 기능을 구현하기 위해 사용

    - 우선순위 큐:  Insert, DeleteMin(or DeleteMax) 연산을 지원하는 추상적은 개념의 자료구조
      - DeleteMin: head에서 tail까지 탐색하면서 최소인 값을 찾고 제거
      - Insert: head 앞에 새로운 노드 추가

  - 보통의 리스트를 마치 최소 힙처럼 다룰 수 있게 해줌 (PriorityQueue 처럼 별개의 자료구조가 아님)

    - `heapq.heappush(heap, value)` : heap에 원소 추가
    - `heapq.heappop(heap)` : heap에서 원소 삭제
    - `heapq.heapify(heap)` : 기존 리스트를 힙으로 변환

  - 최대 힙

    ```python
    import heapq
    
    nums = [4, 1, 7, 3, 8, 5]
    heap = []
    
    for num in nums:
      heapq.heappush(heap, (-num, num))  # (우선 순위, 값)
    
    while heap:
      print(heapq.heappop(heap)[1])  # index 1
    ```

- `bisect` : 이진 탐색(Binary Search) 기능을 제공

- `collections`: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함

  - **Counter**: 반복 가능한(iterable) 객체가 주어졌을때 내부의 원소가 몇번씩 등장했는지 알려줌

  ```python
  from collections import Counter
  
  counter = Counter(['red', 'blue', 'red', 'greed', 'blue', 'blue'])
  print(counter['blue'])	# 'blue'가 등장한 횟수 출력
  print(counter['greed'])	# 'green'가 등장한 횟수 출력
  print(dict)	# 사전 자료형으로 반환 {'red': 2, 'blue': 3, 'green': 1}
  ```

- `math`: 필수적인 수학적 기능 제공

  - 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함
  -  **최대 공약수(GCD)/최소 공배수(LCM)**

  ```python
  import math
  
  # 최소공배수(LCM)를 구하는 함수
  def lcm(a, b):
      return a*b // math.gcd(a,b)		# LCM*GCD = A*B
  
  a = 21
  b = 14
  
  print(math.gcd(21, 14))	# 최대 공약수(GCD) 계산 / 7
  print(lcm(21, 14))	# 최소 공배수(LCM) 계산 / 42
  ```



## 진수 변환

- 파이썬은 기본 10진수이기 때문에 다른 진수는 아래와 같이 접두어가 붙음

  - 2진수: 0b
  - 8진수: 0o
  - 16진수: 0x

- **10진수에서 2진수, 8진수, 16진수 변환**

  - bin(), oct(), hex() 내장 함수 사용 (결과는 전부 문자열 타입)
    - 다른 진수 형태에서 다른 진수로 변환도 가능
  - 다른 진수 형태에서 10진수로 변환할 때는 str() 사용

  

### ■ Logical Operation

- **True / False**

  - 숫자 0 / 빈 딕셔너리 / 빈 리스트 / 빈 문자열 = False
  - 아무 값도 없다는 의미인 None = False
  - 그 외의 모든 숫자 / 딕셔너리 / 리스트 / 문자열 = True

- `or`

  - 앞의 값이 True이면 앖의 값을, 앞의 값이 False 이면 뒤에 값을 따름

  ```python
  a = 1 or 10 
  b = 0 or 10
  
  # a:1, b:10
  print("a:{}, b:{}".format(a,b))	
  ```



### ■ Exception Handling

- **try  except**

  ```python
  try:
      # 에러가 발생할 가능성이 있는 코드
  except Exception:	# Exception: 에러 종류 / 빈칸이어도 됨
      # 에러가 발생 했을 경우 처리할 코드
  ```

- **raise**

  - 사용자가 직접 에러를 발생시키는 기능

  ```python
  try:
      # 에러가 발생할 가능성이 있는 코드
      raise StopIteration		# raise 에러 종류
  except StopIteration:
       # 에러가 발생 했을 경우 처리할 코드
  ```

- 예외 이름(ex. list index out of range) 을 모르는 경우 

  ```python
  try:
      # 에러가 발생할 가능성이 있는 코드
  except Exception as ex:	# 에러 종류
      print(ex)			# ex는 발생한 에러의 이름을 받아오는 변수
  ```



### ■ Class

- 자료형 

  - `type(변수명)` : 자료형 (<class 'str'>, <class 'int'>, <class 'float'>, ...)
  - `isinstance(값, 자료형)` : 자료형 검사 (True, False로 반환)

- 클래스와 인스턴스

  - 클래스: 함수나 변수들을 모아 놓은 집합체

  - 인스턴스: 클래스에 의해 생성된 객체 

    - 인스턴스의 클래스가 같더라도 각자 다른 값을 가질 수 있음

    ```python
    list1 = list("hello")
    list2 = list("hello")
    
    isinstance(list1, list)      #True
    isinstance(list2, list)      #True
    
    print(list1 == list2)        #True     list1과 list2는 같은 값을 가집니다.
    print(list1 is list2)        #False    list1과 list2는 다른 인스턴스입니다.
    ```

- 메소드(Method)

  - 클래스에 묶여서 클래스의 인스턴스와 관계되는 일을 하는 함수 (함수와 다른 개념이지만 혼용해서 사용)
  - `self`
    - 메소드의 첫번째 인자
    - 인스턴스의 매개변수를 전달 할때는 self 매개변수는 생략하고 전달
  - 특수한 메소드
    - `__init__` :  **[초기화 함수]** 인스턴스를 만들 때 실행되는 함수 (생성자)
    - `__str__` : **[문자열화 함수]** 인스턴스 자체를 출력할 때 형식을 지정해주는 함수

- 상속(Inheritance)

  - 자식 클래스(상속 받는 클래스)가 부모 클래스(상속하는 클래스)의 내용을 가져다 쓸 수 있는 것

  ```python
  class Animal():
      def walk(self):
          print("걷는다")
      def eat(self):
          print("먹는다")
          
  class Human(Animal):		# Animal 클래스를 상속받음
      def wave(self):
          print("손을 흔든다")
  
  class Dog(Animal):			# Animal 클래스를 상속받음
      def wag(self):
          print("꼬리를 흔든다")   
          
  person = Human()	# Human 인스턴스 생성
  person.walk()
  person.eat()
  person.wave()
  
  dog = Dog()			# Dog 인스턴스 생성				
  dog.walk()
  dog.eat()
  dog.wag()
  ```

- 오버라이드(Override)

  - 같은 이름을 가진 메소드를 덮어 쓴다는 의미

  ```python
  class Animal():
      def greet(self):
          print("인사한다")
  
  class Human(Animal):
      def greet(self):
          print("손을 흔든다")
          
  class Dog(Animal):
      def greet(self):
          print("꼬리를 흔든다")
  ```

- super()

  - 자식클래스에서 부모클래스의 내용 사용하고 싶은 경우
  - super().부모클래스내용

  ```python
  class Animal( ):
      def __init__( self, name ):			# 클래스 생성자(Constructor)
          self.name = name				# 객체가 생성될 때 자동으로 호출되는 메소드
      def greet(self):
          print("{}이/가 인사한다".format(self.name))
  
  class Human( Animal ):
      def __init__( self, name, hand ):
          super().__init__( name ) 		# 부모클래스의 __init__ 메소드 호출
          self.hand = hand
      
      def wave(self):
          print("{}을 흔들면서".format(self.hand))
      
      def greet(self):
          self.wave()
          super().greet()
  
  person = Human( "사람", "오른손" )
  ```

  


