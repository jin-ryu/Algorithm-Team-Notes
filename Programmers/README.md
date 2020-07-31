## Programmers 문제들



#### 해시(Hash)

- 해시는 Key-value의 쌍으로 데이터를 저장하는 자료구조
- Python에서는 Dictionary를 사용하면 유리



#### 스택(Stack)

- 데이터의 삽입과 삭제가 저장소의 맨 윗 부분에서만 일어나는 자료구조

- **LIFO: Last in First Out**

- 장점: 참조 지역성(한번 참조된 곳은 다시 참조될 확률이 높다)을 활용할 수 있음

- 단점: 데이터를 탐색하기 어려움

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



#### 큐(Queue)

- 목록의 한쪽 끝에서만 자료를 넣고 다른 한쪽 끝에서만 자료를 뺄 수 있는 자료구조

- **FIFO : First in, First out**

- Queue의 ADT(abstract data type)

  - `enqueue()`  : Queue의 끝에 새로운 데이터가 추가
  - `dequeue()` : Queue의 첫번째 위치의 데이터를 삭제

- Queue의 종류 : 선형 큐, 원형 큐, 우선순위 큐

- Queue 구현하기 1 - 리스트

  - **Queue를 리스트로 구현하는 것은 효율적이지 않음**
  - enqueue()의 시간복잡도는 O(1)이며, dequeue는 O(N)
  - 추가의 경우 큐의 맨 끝에서만 일어나니 빠르지만, 큐의 첫번째 원소를 삭제할 경우 두번째 원소부터 맨 마지막 원소까지 모든 원소들의 위치를 왼쪽으로 한 칸씩 옮겨주어야 하기 때문에 느림

  ```python
  class ListQueue(object):
      def __init__(self):
          self.queue = []
         
     	def dequeue(self):
          if not self.queue:		# if len(self.queue) == 0:
              return -1
          self.queue.pop(0)
          
      def enqueue(self, n):
          self.queue.append(n)
      
      def printQueue(self):
          print(self.queue)
          
  if __name__ == "__main__":
      lq = ListQueue()	# 클래스로 생성해서 이후 사용
  ```

- **Queue 구현하기 2 - collections.deque**

  - deque(데크) 
    - double-ended queue의 줄임말로, 앞과 뒤 양방향에서 데이터를 처리할 수 있는 자료구조
    - list와 유사하지만 **앞뒤에서 데이터를 처리하는 속도가 O(1)로 매우 빠름**
      (내부적으로 doublely linked list로 구현되어 있기 때문
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

- Queue 구현하기 2 - Queue 모듈 사용

  - 파이썬의 Queue 모듈에서는 큐(Queue), 우선순위큐(PriorityQueue), 스택(LifoQueue)를 제공하고 있음
  - 특히 큐 모듈은 스레드 환경을 고려하여 작성되어 있기 때문에 여러 스레드에서 동시에 같은 객체에 접근하여 작업을 수행하여도 정상적으로 동작하는 것을 보장

  ```python
  import queue
  
  # Queue 선언
  q = queue.Queue()
  
  # q에 데이터 추가
  q.put(1)
  q.put(2)
  q.put(3)
  q.put(4)
  
  # q에 저장된 데이터 개수	
  print(q.qsize())	# 5
  
  # q의 첫번째 원소 제거
  print(q.get())		# 1
  print(q.get())		# 2
  print(q.get())		# 3
  print(q.get())		# 4
  ```

  

#### 깊이/너비 우선탐색(DFS/BFS)

- BFS(Breadth First Search, 너비 우선 탐색)

  - 큐(queue) 

    - 노드를 방문하면서 인접한 노드 중 방문하지 않았던 노드의 정보를 큐에 삽입	.

      - `set`을 사용하여 구현

      ```python
      graph_list = {1: set([3, 4]),
                    2: set([3, 4, 5]),
                    3: set([1, 5]),
                    4: set([1]),
                    5: set([2, 6]),
                    6: set([3, 5])}
      root_node = 1
      ```

    - 큐에 먼저 들어있던 노드부터 순차적으로 방문

    - 삽입 : `list.append(something)`

    - 삭제 : `list.pop(0)`(시간적으로 비효율적) / `collections.deque()`

  - 구현 방법

    ```python
    from collections import deque
    
    def BFS_with_adj_list(graph, root):
        visited = []
        queue = deque([root])
    
        while queue:
            n = queue.popleft()
            if n not in visited:
                visited.append(n)
                queue += graph[n] - set(visited)
        return visited
      
    print(BFS_with_adj_list(graph_list, root_node))
    ```

- DFS(Depth First Search, 깊이 우선 탐색)

  - 스택(stack)

    - 먼저 방문한 노드에 연결된 노드보다, 현재 방문한 노드에 연결된 노드를 연결해야 한 방향으로 갈 수 있기 때문에 DFS에서는 스택이 유리
    - 삽입 : `list.append(something)`
    - 삭제 : `list.pop(0)`

  - 구현 방법

    ```python
    def DFS_with_adj_list(graph, root):
        visited = []
        stack = [root]
    
        while stack:
            n = stack.pop()
            if n not in visited:
                visited.append(n)
                stack += graph[n] - set(visited)
        return visited
    
    print(BFS_with_adj_list(graph_list, root_node))
    ```

    