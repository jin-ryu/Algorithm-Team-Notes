## 파이썬 알고리즘 개념 정리

#### 알고리즘 복잡도

- 다양한 알고리즘 중 어느 알고리즘이 더 좋은지를 분석하기 위해, 복잡도를 정의하고 계산함

- 알고리즘 복잡도

  - **시간 복잡도**: 알고리즘 실행 속도 **(-> 반복문이 지배)**
  - 공간 복잡도: 알고리즘이 사용하는 메모리 사이즈

- 알고리즘 성능 표기법

  - Big O(빅-오) 표기법: O(N)
    - 알고리즘의 **최악의 실행시간**을 표기
    - 아무리 최악의 상황이라도, 이 정도의 성능을 보장한다는 의미
    - 가장 많이, 일반적으로 사용
  - Ω (오메가) 표기법: Ω(N), 알고리즘 최상의 실행시간을 표기
  - Θ (세타) 표기법: Θ(N), 알고리즘 평균 실행 시간을 표기

- Big O(빅-오) 표기법

  - O(입력): 입력에 따라 결정되는 시간 복잡도 함수

  - $$
    O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(2^n) < O(n!)
    $$

    - 표현식에 가장 큰 영향을 미치는 n의 단위로 표시
      - <small> 빅오 표기법에서 logn 에서의 log의 밑은 10이 아니라, 2 </small>
    - O(1): 무조건 2회(상수번) 실행한다. (n의 값에 영향을 받지 않음)
    - O(n): n에 따라, n번, n+10번 또는 3n+10번 등을 실행한다.
    - O(n^2): n^2번, n^2 + 1000 번, 또는 100n^2 - 100 번등 실행한다.



#### 배열(Array)

- 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조

- 파이썬에서는 **List 타입**이 배열 기능을 제공하고 있음

- 같은 종류의 데이터를 **순차적으로 저장**해 효율적으로 관리하기 위해 사용

- 배열의 장점

  - 빠른 접근 가능

- 배열의 단점

  - 추가/삭제가 쉽지 않음
  - 미리 최대 길이를 지정해야 함 (List는 예외)

  

#### 큐(Queue)

- 목록의 한쪽 끝에서만 자료를 넣고 다른 한쪽 끝에서만 자료를 뺄 수 있는 자료구조

- FIFO(First in, First out) 또는 LILO(Last in, Last out) 방식

- Queue의 ADT(abstract data type)

  - `enqueue()`  : Queue의 끝에 새로운 데이터가 추가
  - `dequeue()` : Queue의 첫번째 위치의 데이터를 삭제

- 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용 
  (프로세스 스케쥴링 방식을 함께 이해해두는 것이 좋음)

- Queue의 종류 : 선형 큐, 원형 큐, 우선순위 큐

- Queue 구현하기 1 - 리스트

  - **Queue를 리스트로 구현하는 것은 효율적이지 않음**

  - enqueue()의 시간복잡도는 O(1)이며, dequeue는 O(N)

    - enqueue()의 경우 큐의 맨 끝에서만 일어나니 빠름
    - 첫번째 원소를 dequeue() 할 경우 두번째 원소부터 맨 마지막 원소까지 모든 원소들의 위치를 왼쪽으로 한 칸씩 옮겨주어야 하기 때문에 느림

    ```python
    queue_list = list()
    
    def enqueue(data):
        queue_list.append(data)
        
    def dequeue():
        data = queue_list[0]
        del queue_list[0]
        return data
    
    # 0~9까지 10개의 숫자 삽입
    for index in range(10):
        enqueue(index)
    
    len(queue_list)		# Out: 10
    dequeue()			# Out: 0
    ```

- **Queue 구현하기 2 - Queue 모듈 사용**

  - 스레드 환경을 고려하여 작성되어 있기 때문에 여러 스레드에서 동시에 같은 객체에 접근하여 작업을 수행하여도 정상적으로 동작하는 것을 보장

  - Queue 모듈에서는 큐(Queue), 우선순위큐(PriorityQueue), 스택(LifoQueue)를 제공

    - Queue(): 가장 일반적인 큐 자료구조

    ```python
    import queue
    
    data_queue = queue.Queue()
    data_queue.put("funcoding")
    data_queue.put(1)
    
    data_queue.qsize()	# Out: 2
    
    data_queue.get()	# Out: funcoding
    data_queue.get()	# Out: 1
    ```

    - PriorityQueue(): 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력

    ```python
    import queue
    
    data_queue = queue.PriorityQueue()
    
    # 앞의 숫자: 우선순위, 뒤의 값: 입력 데이터
    data_queue.put((10, "korea"))
    data_queue.put((5, 1))
    data_queue.put((15, "china"))
    
    data_queue.qsize()	# Out: 3
    
    data_queue.get()	# Out: (5,1)
    data_queue.get()	# Out: (10, "korea")
    ```

    - LifoQueue(): 나중에 입력된 자료가 먼저 출력되는 구조 (스택 구조)

    ```python
    import queue
    
    data_queue = queue.LifoQueue()
    data_queue.put("funcoding")
    data_queue.put(1)
    
    data_queue.qsize()	# Out: 2
    
    data_queue.get()	# Out: 1
    ```


- **Queue 구현하기 3 - collections.deque**

  - deque(데크) 
    - double-ended queue의 줄임말로, 앞과 뒤 양방향에서 데이터를 처리할 수 있는 자료구조
    - list와 유사하지만 **앞뒤에서 데이터를 처리하는 속도가 O(1)로 매우 빠름**
      (내부적으로 doublely linked list로 구현되어 있기 때문)
    - Methods
      - `dq.append(value)` : deque의 오른쪽(마지막)에 추가(삽입)
      - `dq.appendleft(value)` : deque의 왼쪽(맨 앞쪽)에 추가(삽입)
      - `dq.extend(iterable)` : iterable argument(list, str, tuple, ...)를 오른쪽(마지막)에 elements를 추가(삽입)
      - `dq.extendleft(iterable)` : 왼쪽(맨 앞쪽)에 데이터를 추가(삽입)
      - `dq.pop()` : 오른쪽(마지막)에서 부터 차례대로 제거와 반환 (remove and return)
      - `dq.popleft()` : 왼쪽(앞쪽)에서 부터 차례대로 제거와 반환 (remove and return)
      - `dq.rotate(n)` : 요소들(elements)을 값만큼 회전해줌
        값이 음수이면 왼쪽으로 회전하고 양수이면 오른쪽으로 회전

  ```python
  from collections import deque 
  
  # deque 선언
  dq = deque([])
  
  # dq에 데이터 추가
  dq.append(1)
  dq.append(2)
  dq.append(3)
  dq.append(4)
  print(dq)		# deque([1,2,3,4])
  
  # dq의 첫번째 원소 제거
  print(dq.popleft())		# 1
  print(dq.popleft())		# 2
  print(dq.popleft())		# 3
  print(dq.popleft())		# 4
  print(dq)		# deque([])
  ```



#### 스택(Stack)

- 데이터의 삽입과 삭제가 저장소의 맨 윗 부분에서만 일어나는 자료구조

- LIFO(Last in, First Out) 또는 FILO(First in, Last Out)

- 스택 구조는 프로세스 실행 구조의 가장 기본

  ```python
  # 재귀 함수
  def recursive(data):
      if data < 0:
          print ("ended")
      else:
          print(data)
          recursive(data - 1)
          print("returned", data)  
  
  # 함수 호출
  recursive(4)
  ```

- 스택의 장점

  - 참조 지역성(한번 참조된 곳은 다시 참조될 확률이 높다)을 활용할 수 있음
  - 구조가 단순해서 구현이 쉬움
  - 데이터 저장/읽기 속도가 빠름

- 스택의 단점 (일반적인 스택 구현 시)

  - 데이터를 탐색하기 어려움
  - 데이터의 최대 갯수를 미리 정해야 함
    - 파이썬의 경우 재귀함수는 1000번까지만 호출 가능함
  - 저장 공간의 낭비가 발생할 수 있음
    - 미리 최대 갯수 만큼의 저장공간을 확보해야 함

- Stack의 ADT(abstract data type)

  - **`push()` **:  맨 위에 값 추가
  - **`pop()`** : 가장 최근에 넣은 맨 위의 값을 제거
  - `peak()` : 스택의 변형 없이 맨위의 값을 출력
  - `is_empty()` : 스택이 비어있는지 확인

- Stack 구현하기 1  - 리스트 사용

  ```python
  stack = []
  stack.append(1)		# push()
  stack.append(2)		# push()
  print(stack)
  print(stack.pop())	# pop(): 2가 출력
  print(stack.pop())	# pop(): 1이 출력
  ```

- Stack 구현하기 2 - 클래스 활용

  ```python
  class Stack(list):
      def __init__(self):
          self.stack=[]
          
      def puch(self, data):
          self.stack.append(data)
          
      def pop(self):
          if self.is_empty():
          	return -1
          return self.stack.pop()
      
      def peek(self):
          return self.stack[-1]
      
      def is_empty(self):
          if len(self.stack) == 0:
              return True
          return False
      
  if __name__ == "__main__":
      s = Stack()
      s.push(1)
      s.push(2)
      s.push(3)
      print(s.peek())		# 3
      print(s.pop())		# 3
      print(s.pop())		# 2
      print(s.pop())		# 1
      print(s.pop())		# -1 (더 이상 존재하지 않음)
  ```



#### 연결 리스트(Linked List)

- 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조

- 연결 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결하여 관리하는 데이터 구조

- 본래 C언어에서는 주요한 데이터 구조이지만, **파이썬은 List 타입이 연결 리스트의 기능을 모두 지원**

- 연결 리스트 기본 구조와 용어

  - 노드(Node): 데이터 저장 단위(데이터 값, 포인터)로 구성
  - 포인터(pointer): 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

- 보통 파이썬에서 연결 리스트를 구현 시, 클래스를 활용

  ```python
  class Node:
      def __init__(self, data):
          self.data = data
          self.next = None
          
  # Node와 Node 연결하기
  node1 = Node(1)
  node2 = Node(2)
  node1.next = node2
  head = node1
  ```

  ```python
  # 데이터 추가하기
  def add(data):
      node = head
      while node.next:
          node = node.next
      node.next = Node(data)
     
  node1 = Node(1)
  head = node1
  for index in range(2, 10):
      add(index)
  ```

  ```python
  # 데이터 검색하기
  node = head
  while node.next:
      print(node.data)
      node = node.next
  print (node.data)
  ```

  

#### 해시(Hash)

- Key-value의 쌍으로 데이터를 저장하는 자료구조

- **파이썬에서는 해시를 별도로 구현할 필요 없이 Dictionary 타입을 사용하면 됨**

  - `del(dict['one'])`  /`dict.pop('two')` : key 값에 따른 삭제
  - `dict.keys()` : key 값들을 dict_keys 객체의 형태로 반환 (리스트로 반환X)
  - `dict.values()` : value 값들을 dict_values 객체의 형태로 반환 (리스트로 반환X)
  - `dict.items()` : key, value 값들을 dict_items 객체의 형태로 반환 (리스트로 반환X)
    * 자주 사용하는 방식 : `for key, value in dict.items():`
  - `zip(*iterables)` : Key 리스트와 Value 리스트로 딕셔너리 생성할 수 있음
    - 두개의 문자열을 비교할 때 이중 for문 사용하는 대신 dictionary의 key, value로 묶어 비교할 수 있음 (ex. zip(list, list[1:]))

- 해시의 기본 용어

  - 해시(Hash): 임의의 값을 고정 길이로 변환하는 것
  - 해시 테이블(Hash Table): 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
  - 해싱 함수(Hashing Function): 키에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
  - 해시 값(Hash Value) / 해시 주소(Hash Address): 키를 해싱 함수로 연산하여 해시 값을 알아 내고, 이를 기반으로 해시 테이블에서 해당 키에 대한 데이터 위치를 일관성 있게 찾을 수 있음
  - 슬롯(Slot):  한 개의 데이터를 저장할 수 있는 공간

- 해시의 장점

  - 데이터 저장/읽기 속도가 빠름 (검색 속도가 빠름)
  - 키에 대한 데이터가 있는지 확인 또는 중복 확인이 쉬움

- 해시의 단점

  - 일반적으로 저장공간이 좀 더 많이 필요
  - 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도의 자료구조가 필요함

- 해시의 주요 용도

  - 검색이 많이 필요한 경우
  - 저장, 삭제, 읽기가 빈번한 경우
  - 캐쉬 구현 시(중복 확인이 쉽기 때문에)

- 시간 복잡도

  - 일반적인 경우(Collision이 없는 경우)는 O(1)
  - 최악의 경우(Collision이 모두 발생하는 경우)는 O(n)

- Hash 구현하기 - 리스트 활용

  - 해시 함수: key%8
    <small> 다양한 해시 함수 고안 기법이 있으며, 가장 간단한 방식이 Division 법 (나누기를 통한 나머지 값을 사용하는 기법) </small>
  - 해시 키 생성: hash(data)

  ```python
  hash_table = list([i for i in range(8)])	# [0, 0, 0, 0, 0, 0, 0, 0]
  
  def get_key(data):
  	return hash(data)
  
  def hash_function(key):
      return key%8
  
  def save_data(data, value):
      hash_address = hash_function(get_key(data))
      hash_table[hash_address] = value
      
  def read_data(data):
      hash_address = hash_function(get_key(data))
      return hash_table[hash_address]
  
  save_data('Dave', '0102030200')
  save_data('Andy', '01033232200')
  read_data('Dave')			# Out: '0102030200'
  
  print(hash_table)			
  # Out: ['0102030200', 0, 0, 0, 0, 0, 0, '01033232200']
  ```



#### 트리(Tree)

- Node와 Branch를 이용해서 사이클을 이루지 않도록 구성한 데이터 구조
- 트리 중 이진 트리(Binary Tree)의 형태의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용
- 트리의 기본 용어
  - Node: 데이터와 다른 연결된 노드에 대한 Branch 정보를 저장하는 기본 요소
  - Root Node: 트리의 맨 위에 있는 노드
  - Level: 최상위 노드를 Level 0으로 하였을 때, 하위 Branch로 연결된 노드의 깊이
  - Parent Node: 어떤 노드의 다음 레벨에 연결된 노드
  - Child Node: 어떤 노드의 상위 레벨에 연결된 노드
  - Leaf Node(Terminal Node): Child Node가 하나도 없는 노드
  - Sibling(Brother Node): 동일한 Parent Node를 가진 노드
  - Depth: 트리에서 Node가 가질 수 있는 최대 Level
- **이진트리(Binary Tree)와 이진 탐색 트리(Binary Search Tree, BST)**
  - 이진 트리(Binary Tree): 노드의 최대 Branch가 2인 트리
  - 이진 탐색 트리(Binary Search Tree, BST): 왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드은 해당 노드보다 큰 값을 가지고 있는 이진 트리
  - 주요 용도: 데이터 검색(탐색)
  - 이진 탐색 트리의 장점 
    - 탐색 속도를 개선할 수 있음
      - depth(트리의 높이)를 h라고 표기한다면, O(h)
      - h = logn에 가까우므로, 시간 복잡도는 O(logn)
      - 한번 실행 할 때마다 50%의 실행할 수도 있는 명령을 제거한다는 의미. 즉 50%의 실행 시간을 단축시킬 수 있다는 것을 의미함
  - 이진 탐색 트리의 단점
    - 평균 시간 복잡도는 O(logn)이지만, 최악의 경우 O(n)
      
      - <small> 최악의 경우: 한쪽 노드만 있는 트리</small>
      
      

#### 힙(Heap)

- **최댓값 or 최솟값**을 찾아내는 연산을 빠르게 하기 위해 고안된 **완전 이진 트리(Complete Binary Tree)**를 기본으로 한 자료구조

  - 완전 이진 트리(Complete Binary Tree)
    - 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리

- 힙의 종류

  - 최대 힙 : key(T.parent(v)) > key(v),  부모 노드의 키 값이 자식 노드의 키 값보다 항상 큰 힙
  - 최소 힙 : key(T.parent(v)) < key(v), 부모 노드의 키 값이 자식 노드의 키 값보다 항상 작은 힙
  - 원소 값의 대소 관계는 부모-자식 노드 간에만 성립 (형제 노드 사이에는 X)

- 가장 높은(혹은 가장 낮은) 우선순위를 가지는 노드가 항상 루트 노드에 옴

- **시간 복잡도 = 삽입/삭제 O(log n)** 

  - 삽입/삭제 시 전체 원소의 반만큼의 값과 비교하기 때문

- 힙과 이진 탐색 트리의 공통점과 차이점

  - 공통점: 이진 트리
  - 차이점
    - 힙은 각 노드의 값이 자식 노드보다 크거나 같음(Max Heap의 경우)
    - 이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고, 그 다음 부모 노드, 그 다음 자식 노드 값이 가장 큼
    - 힙은 이진 탐색 트리의 조건인 자식 노드에서 작은 값은 왼쪽, 큰 값은 오른쪽이라는 조건은 없음
      - 힙의 왼쪽 및 오른쪽 자식 노드의 값은 오른쪽이 클수도, 왼쪽이 클수도 있음
    - 이진 탐색 트리는 탐색을 위한 구조, 힙은 최대/최소값 검색을 위한 구조 중 하나

- 연산 구현 방법

  - 삽입 연산 (insertion)
    - 삽입하고자 하는 값을 트리의 가장 마지막 원소에 추가
    - 부모노드와 대소관계를 비교하면서 만족할 때 까지 자리 교환을 반복
  - 삭제 연산 (deletion)
    - 힙에서는 루트 노드만 삭제가 가능하므로 루트 노드를 제거
    - 가장 마지막 노드를 루트로 이동
    - 자식노드와 비교하여 조건이 만족할 때까지 이동

- MaxHeap 구현하기 - list

  - 배열(리스트)은 인덱스가 0부터 시작하지만, 힙 구현의 편의를 위해 root 노드 인덱스 번호를 1로 지정하면 구현이 좀 더 수월함
  - i번째 노드의 왼쪽 자식 노드의 위치는 2i+1
  - i번째 노드의 오른쪽 자식 노드의 위치는 2i+2
  - i번째 노드의 부모 노드의 위치는 (i-1)//2

- Heap 구현하기 - heapq module

  - heapq module : 일반적인 리스트를 min heap 처럼 다룰 수 있게 해줌

  -  `heappush(heap, value)` : 노드 추가

    - 시간 복잡도 :  O(log n)

    ```python
    heap = []
    heap.heappush(heap, 1)
    ```

  - `heappop(heap)` : 노드 삭제

    - 시간 복잡도 :  O(log n)
    - 가장 작은 원소를 꺼내 리턴, 자동적으로 그 다음 작은 원소가 루트 노드가 됨
    - **인덱스 1이 2번째로 작다는 보장은 없으므로 n번째로 작은 원소를 알고 싶다면 n-1개의 원소를 빼내야 함**

    ```python
    return heapq.heappop(heap)
    
    # 최소값을 꺼내지 않고 리턴만 하려면 인덱스로 접근하기
    print(heap[0])
    ```

  - `heapify(list)` : 기존에 사용한 리스트를 힙으로 변환하기 (min heap에 맞게 재정렬)

    - 시간 복잡도 : O(n)

  - 최대 힙 만들기: 우선순위가 포함된 튜플 이용하기

    - 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리	

    ```python
    import heapq
    
    nums = [4, 1, 7, 3, 8, 5]
    heap = []
    
    for num in nums:
        heapq.heappush(heap, (-num, num))  	# (우선 순위, 값)
    
    while heap:
        print(heapq.heappop(heap)[1])  		# index 1
    ```

  - K번째 최소값/최대값

    - K번째 최소값을 구하기 위해서는 주어진 배열로 힙을 만든 후, `heappop()` 함수를 k번 호출하면 됨

    ```python
    import heapq
    
    def kth_smallest(nums, k):
      heap = []
      for num in nums:
        heapq.heappush(heap, num)
    
      kth_min = None
      for _ in range(k):
        kth_min = heapq.heappop(heap)
      return kth_min
    
    print(kth_smallest([4, 1, 7, 3, 8, 5], 3))
    ```



#### 버블 정렬(Bubble sort)

- 두 인접한 데이터를 비교해서,  앞에 있는 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘 

- n개의 리스트가 있는 경우 최대 n-1번 로직을 적용한다.

- 로직을 1번 적용할 때마다 가장 큰 숫자가 뒤에서 부터 1개씩 결정된다.

- 로직이 경우에 따라 일찍 끝날 수도 있다. 따라서 로직을 적용할 때 한번도 데이터가 교환된 적이 없다면 이미 정렬 된 상태이므로 더 이상 로직을 반복할 필요 없다.

- 예시: [1, 9, 3, 2]

  - 1st: [1, 9, 3, 2] [1, 3, 9, 2] [1, 3, 2, 9]
  - 2nd: [1, 3, 2, 9] [1, 2, 3, 9] [1, 2, 3, 9]
  - 3rd: [1, 2, 3, 9] [1, 2, 3, 9] [1, 2, 3, 9]

- 구현 : **O(n^2)**

  ```python
  def bubble_sort(data_list):
      for index in range(len(data_list)):	# 시작 시점
          swap = 0
          for index2 in range(len(data_list)-1-index):	# 반복 횟수
              if data_list[index] > data_list[index+1]:
                  data_list[index], data_list[index+1] = data_list[index+1], data_list[index+1] 
                  swap += 1
          if swap == 0:	# swap을 한번도 하지 않았다면 이미 정렬된 것이므로 종료
              break
              
  	return list
  ```

  

#### 삽입 정렬(Insertion sort)

- key 값을 설정해, **key 값 앞에 있는 숫자들 중 key의 위치를 찾아 삽입**하는 정렬 알고리즘

- 두번째 인덱스부터 시작

- 해당 인덱스(key 값) 앞에 있는 데이터(B)부터 비교해서 key 값이 더 작으면, B값을 뒤 인덱스로 복사

- 이를 key 값이 더 큰 데이터를 만날때까지 반복하고, 큰 데이터를 만난 위치 바로 뒤에 key 값을 이동

- 예시: [9, 3, 2, 5]

  - key = 9: [9, 3, 2, 5]
  - key = 3: [3, 9, 2, 5]
  - key = 2: [3, 2, 9, 5] [2, 3, 9, 5]
  - key = 5: [2, 3, 5, 9]

- 구현 : **O(n^2)**

  ```python
  def insertion_sort(data_list):
      for key in range(len(data_list)):
          for index in range(key, 0, -1):
              # key 값보다 작은 값을 만나면 그 값과 뒤의 값을 교환
              if key < list[index-1]:
                  data_list[index], data_list[index-1] =  data_list[index-1], data_list[index]
              else:
                  break
                  
       return list   
  ```



#### 선택 정렬(Selection sort)

- 주어진 데이터 중 **최소값**을 찾아 **맨 앞에 위치한 값과 교체**하는 과정을 반복하며 정렬하는 알고리즘

- 예시: [9, 3, 2, 1]

  - [1, 3, 2, 9] : 1, 9를 swap
  - [1, 2, 3, 9] : 2, 3을 swap
  - [1, 2, 3, 9] : 변화 없음

- 구현 : **O(n^2)**

  ```python
  def selection_sort(data_list):
      for index in range(len(data_list)-1):
          lowest = index
          for index2 in range(index, len(data_list)):
              if data_list[lowest] > data_list[index2]:	# 해당 범위에서 최소값을 찾음
                  lowest = index2
          # 최소값과 맨 앞의 값을 교환        
          data_list[index], data_list[lowest] = data_list[lowest], data_list[index]
     	    
      return list
  ```

  

#### 재귀 용법 (Recursive call)

- 함수 안에서 동일한 함수를 호출하는 형태

- 재귀 호출은 **스택**의 전형적인 예

- 예시 : 팩토리얼

  - 일종의 n-1번 반복문을 호출한 것과 동일
  - factorial() 함수를 호출할 때마다, 지역변수 n이 생성됨
  - 시간, 공간 복잡도 모두 O(n-1) = O(n)

  ```python
  def factorial(num):
      if num > 1:
          return num * factorial(num-1)
      return num
  ```

- 예시 :  1부터 num까지의 곱을 출력하는 함수

  ```python
  def multiple(data):
      if data <= 1:
          return data
      return data * multiple(data-1)
  ```

- 예시 : 리스트의 합을 리턴하는 함수

  ```python
  def sum_list(data):
      if len(data) == 1:
          return data[0]
      return data[0] + sum_list(data[1:])
  ```

- 예시 : 회문(palindrome)을 판별하는 함수

  - <small>회문(palindrome): 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장 </small>

  ```python
  def recursive(string):
      if len(string) == 1:
          return True
      
      if string[0] == string[-1]:
          return recursive(string[1:-1])
      else:
          return False
  ```

- 예시: n이 홀수이면 3n+1, n이 짝수이면 n//2를 n이 1이 될때까지 반복하는 함수

  ```python
  def func(n):
      if n == 1:
          return 
      
      if n%2 == 1:
          return func(3*n+1)
      else:
          return func(n//2)
  ```

- 예시: 정수 n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수를 구하는 함수

  - 정수 n을 만들 수 있는 경우의 수를 리턴하는 함수를 f(n) 이라고 하면,
    f(n)은 f(n-1) + f(n-2) + f(n-3) 과 동일하다는 패턴 찾기

  ```python
  def f(n):
      if n < 0:
          return 0
      elif n == 1:
          return 1
      elif n == 2:
          return 2
      elif n == 3:
          return 4
      else:
          return f(n-1) + f(n-2) + f(n-3)
      
  ```



#### 동적 계획법(Dynamic Programming)과 분할 정복(Divide and Conquer)

- 동적 계획법(Dynamic Programming)

  - 입력 크기가 작은 부분 문제들을 해결한 후, 보다 큰 크기의 부분 문제를 해결하여 최종적으로 전체 문제를 해결하는 알고리즘
  - 상향식 접근법으로, **가장 최하위 해답을 구한 후 해당 결과값을 이용해서 상위 문제를 풀어가는 방식**
  - Memoization 기법을  사용
    - <small> Memoization: 프로그램 실행 시 이전에 계산한 값을 저장하여, 다시 계산하지 않도록 하여 전체 실행 속도를 빠르게 하는 기술</small>
  - 문제를 잘게 쪼갤 때, 부분 문제를 중복되어 재활용 됨 (ex. 피보나치 수열)

- 분할 정복(Divide and Conquer)

  - 문제를 나눌 수 없을 때까지 나누어서 각각을 풀면서 다시 합병하여 문제의 답을 얻는 알고리즘
  - 하향식 접근법으로, **상위의 해답을 구하기 위해서 아래로 내려가면서 하위의 해답을 구하는 방식**
  - 일반적으로 재귀함수로 표현
  - 문제를 잘게 쪼갤 때, 부분 문제는 서로 중복되지 않음 (ex. 병합 정렬, 퀵 정렬)

- 공통점과 차이점

  - 공통점
    - 문제를 잘게 쪼개서, 가장 작은 단위로 분할
  - 차이점
    - 동적 계획법
      - 부분 문제는 중복되어 상위 문제 해결 시 재활용 됨
      - Memoization 기법 사용 (부분 문제의 해답을 저장해서 재활용하는 최적화 기법)
    - 분할 정복
      - 부분 문제는 서로 중복되지 않음
      - Memoization 기법 사용 안함

- 예시: 피보나치 수열 

  - recursive call 활용

  ```python
  def fibo(num):
      if num <= 1:
          return num
      return fibo(num - 1) + fibo(num - 2)
  ```

  - 동적 계획법 활용

  ```python
  def fibo_dp(num):
      cache =  [ 0 for index in range(num + 1) ]	# num+1개의 0 초기화
      cache[0] = 0
      cache[1] = 1
      
      for index in range(2, num + 1):	# 이전 cache를 활용해 다음 cache를 구함
          cache[index] = cache[index - 1] + cache[index - 2]
      return cache[num]
  ```



#### 병합정렬(Merge sort)

- 재귀 용법을 활용한 정렬 알고리즘

- 리스트를 동일한 크기의 부분 리스트로 나눠(숫자가 하나 남을때까지), 각 부분 리스트를 재귀적으로 합병정렬을 이용해 정렬하여 다시 하나의 정렬된 리스트로 합병한다.

- 예시 : [1, 9, 3, 2]

  - [1, 9] [3, 2]로 분할
  - [1], [9]로 나누고 다시 정렬해서 합침 [1, 9]
  - [3], [2]로 나누고 다시 정렬해서 합침 [2, 3]
  - [1, 9] [2, 3]을 합침
    - 1 < 2: [1]
    - 9 > 2: [1, 2]
    - 9 > 3: [1, 2, 3]
    - 9만 남음: [1, 2, 3 ,9]

- 구현 : **O(nlogn)**

  ```python
  merge_split(data_list):	# 리스트 분할 함수
      if len(data_list) ==  1:
          return data_list
      medium = len(data_list)//2
      left = merge(data_list(:medium))
      right = merge(data_list(medium:))
      
      return merge(left, right)
  
  def merge(left, right):		# 데이터를 정렬하여 합병하는 함수
  	merged = []
      left_point, right_point = 0
      
      # left/right 둘 다 있을 때
      while len(left) > left_point and len(right) > right_point:
          if left[left_point] > right[right_point]:
              merged.append(right[right_point])
              right_point += 1
          else:
              merged.append(left[left_point])
              left_point += 1
              
      # left 데이터가 없을 때
      while len(left) > left_point:
          merged.append(left[left_point])
          left_point += 1
      
      # right 데이터가 없을 때
      while len(right) > right_point:
          merged.append(right[right_point])
          right_point += 1
          
      return merged
  ```

  

#### 퀵 정렬(Quick sort)

- 재귀 용법을 활용한 정렬 알고리즘

- 기준점(pivot)을 정해 기준점보다 작은 데이터는 왼쪽(left),  큰 데이터는 오른쪽(right)으로 모으는 함수를 작성함

- 각 왼쪽(left), 오른쪽(right)은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복함

- 함수는 왼쪽(left) + 기준점(pivot) +  오른쪽(right)을 리턴함

- 구현 **: O(nlogn)**

  ```python
  def quick_sort(data_list):
      if len(data_list) ==  1:
          return data_list
      
      left, right = [], []
      pivot = data_list[0]	# 기준점을 리스트 맨 앞 원소로 잡음
      
      for index in range(1, len(data_list)):
          if pivot > data_list[index]:
              left.append(data_list[index])
          else:
              right.append(data_list[index])
      
      return quick_sort(left) + [pivot] + quick_sort(right)
  ```




#### 이진 탐색(Binary Search)

- 탐색할 자료를 둘로 나누어 해당 데이터가 있을만한 곳을 탐색하는 방법

- 이진 탐색은 **데이터가 정렬되어 있는 상태**에서 진행

- 분할 정복 알고리즘과 이진 탐색

  - 분할 정복 알고리즘(Divide and Conquer)
    - Divide: 문제를 하나 또는 둘 이상으로 나눈다.
    - Conquer: 나눠진 문제가 충분히 작고, 해결이 가능하다면 해결하고, 그렇지 않다면 다시 나눈다.
  - 이진 탐색
    - Divide: 리스트를 두 개의 서브 리스트로 나눈다.
    - Conquer
      - 검색할 숫자(search) == 중간값 이면, 탐색을 종료한다.
      - 검색할 숫자(search) > 중간값 이면, 뒷 부분의 서브 리스트에서 검색할 숫자를 찾는다.
      - 검색할 숫자(search) < 중간값 이면, 앞 부분의 서브 리스트에서 검색할 숫자를 찾는다.

- 구현: **O(logn)**

  ```python
  def binary_search(data, search):
      # 예외 처리
      if len(data) == 0:
          return False
      if len(data) == 1:
          if data[0] == search:
              return True
          else:
              return False
          
      # 메인 로직
      mid = len(data)//2
      if search > data[mid]:
          return binary_search(data[mid:], search)
      elif search < data[mid]:
        	return binary_search(data[:mid], search)
      else:
          return True
  ```

  

#### 깊이/너비 우선탐색(DFS/BFS)

- 파이썬으로 그래프를 표현하는 방법

  - 딕셔너리와 리스트를 활용하여 표현

    - 노드: 딕셔너리 key
    - 간선: 딕셔너리 value (연결된 노드들의 리스트)

    ```python
    graph = dict()
    
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'G', 'H', 'I']
    graph['D'] = ['B', 'E', 'F']
    graph['E'] = ['D']
    graph['F'] = ['D']
    graph['G'] = ['C']
    graph['H'] = ['C']
    graph['I'] = ['C', 'J']
    graph['J'] = ['I']
    ```

- BFS(Breadth First Search, 너비 우선 탐색)

  - 정점들과 같은 레벨에 있는 노드들 (형제 노드들)을 먼저 탐색하는 방식

  - need_visit **큐**와 visited **큐**를 활용

  - 구현:  O(V+E) <small> V는 노드 수, E는 간선 수</small>

    ```python
    from collections import deque 
    
    def bfs(graph, start_node):
        visited = deque([])
        need_visit = deque([])
        need_visit.append(start_node)	# 시작 노드 삽입
        
        while need_visit:
            node = need_visit.popleft()	# 리스트의 시작 원소를 방문(큐의 rear)
            if node not in visited:
                visited.append(node)
                need_visit.extend(graph[node])
        
        return list(visited)	# 노드 방문 순서
    ```

    - 큐를 구현할 때 `collections.deque`나 `queue` 모듈을 사용해도 됨

- DFS(Depth First Search, 깊이 우선 탐색)

  - 정점의 자식들을 먼저 탐색하는 방식

  - need_visit **스택**과 visited **큐** 이용

  - 구현: O(V+E) <small> V는 노드 수, E는 간선 수</small>

    ```python
    def dfs(graph, start_node):
        visited, need_visit = list(), list()	# 큐, 스택
        need_visit.append(start_node)	# 시작 노드 삽입
        
        while need_visit:
            node = need_visit.pop()	# 리스트의 끝 원소를 방문(스택 top)
            if node not in visited:
                visited.append(node)
                need_visit.extend(graph[node])	# 다음 레벨에 있는 노드들을 need_visit에 추가
                
        return visited	# 노드 방문 순서
    ```

    - 큐를 구현할 때 `collections.deque`나 `queue` 모듈을 사용해도 됨

  
