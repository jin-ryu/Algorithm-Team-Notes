# Python Introduction

###### 💁 유찌니의 파이썬 노트



### ■ String

- **Methods**

  - `string.split(str)` :  str 기준으로 문자열을 분리하여 리스트를 생성
  - `format()` : 포맷팅을 수행 / 중괄호 {}를 이용해 값을 대입
    - `print('My name is {} and I'm {} years old.format(Jin, 24))`
  - `end` : print() 함수에서 출력의 끝을 지정
    - `print('Python Introduction' , end='')`

  


### ■ List

- **Methods**
  - `list1.append(value)` : 리스트에 새로운 값이 추가
  - `list1.extend([value1, value2, ...])` : 리스트 뒤에 값을 추가
  - `list1.index(value)` : 값을 이용하여 위치를 찾는 기능
  - `list1.insert(index, value)` : 원하는 위치에 값을 추가
  - `list1.remove(value)` : 특정 값을 지움
    (여러개의 값이 있는 경우 가장 앞에 있는 하나만 지워짐)
  - `list1.count(value)` : 해당 값을 개수를 셈 
  - `list1.sort()` : 값을 순서대로 정렬 (list1의 원래값이 변함)
  - `list1.reverse()` : 값을 역순으로 정렬 (list1의 원래값이 변함)
  - `list2 = sorted(list1)` : 값을 순서대로 정렬 (list1의 원래값이 변하지 않음)
  - `if value in list1` : 리스트 안에 값이 들어있는지 확인 
  - `if valie not in list1` : 리스트 안에 값이 들어있지 않은 지 확인 
  - `del list1[index]` : 특정 위치의 값을 지움
  - `enumerate(list1)` : index와 value를 tuple 형태로 반환
    - 반복문 사용 시 몇 번째 반복문인지 확인할 필요가 있을 때 사용
    - 자주 사용하는 방식: `for index, value in enumerate(list1):`
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



### ■ Dictionary

- **Methods**
  - `del(dict['one'])`  /`dict.pop('two')` : key 값에 따른 삭제
  - `dict.keys()` : key 값들을 dict_keys 객체의 형태로 반환 (리스트로 반환X)
  - `dict.values()` : value 값들을 dict_values 객체의 형태로 반환 (리스트로 반환X)
  - `dict.items()` : key, value 값들을 dict_items 객체의 형태로 반환 (리스트로 반환X)
    * 자주 사용하는 방식: `for key, value in dict.items():`
- **List vs. Dictionary**
  ![리스트와 딕셔너리 비교](https://user-images.githubusercontent.com/45402031/88435926-2f97e780-ce3e-11ea-8e1d-8d6ce975b1e0.png)



### ■ Tuple

- 한번 정해진 순서를 바꿀 수 없다

- 튜플의  값은 변경과 삭제가 불가능

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



### ■ Logical Operation

- true, false

  - 숫자 0 / 빈 딕셔너리 / 빈 리스트 / 빈 문자열 = false
  - 아무 값도 없다는 의미인 None = false
  - 그 외의 모든 숫자 / 딕셔너리 / 리스트 / 문자열 = true

- `or`

  - 앞의 값이 true이면 앖의 값을, 앞의 값이 false 이면 뒤에 값을 따름

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









*__reference link :__*

Programmers 파이썬 입문:  <https://programmers.co.kr/learn/courses/2>

Programmers 김왼손의 왼손코딩: <https://programmers.co.kr/learn/courses/29>

