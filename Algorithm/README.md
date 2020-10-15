# Python Algorithm

💁 유찌니의 알고리즘 노트

- [그리디](#Greedy)
- [구현](#Implementation)
- [DFS/BFS](#DFS/BFS)
- 정렬
- 이진 탐색
- 다이나믹 프로그래밍
- 최단 경로
- 기타 그래프 이론



## 알고리즘 설계 Tip

- 일반적으로 CPU 기반의 개인 컴퓨터나 채점용 컴퓨터에서 연산 횟수가 5억을 넘어가는 경우
  - C언어를 기준으로 통상 1~3초 가량의 시간이 소요
  - Python을 기준으로 통상 5~15초 가량의 시간이 소요
    - Pypy의 경우 때때로 C언어보다도 빠르게 동작하기도 함
- O(N<sup>3</sup>)의 알고리즘을 설계한 경우, N의 값이 5,000이 넘는다면 얼마나 걸릴까요?
- **코딩 테스트 문제에서 시간 제한은 통상 1~5초 가량**이라는 점을 유의
  - 혹여 문제에 명시되어 있지 않은 경우 대략 5초 정도라고 생각하고 문제를 푸는 것이 합리적



## Greedy

#### 그리디 알고리즘(탐욕법)

- **현재 상황에서 지금 당장 좋은 것만 고르는 방법**
- 일반적으로 문제를 풀기  위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
- 그리디 해법은 그 정당성 분석이 중요
  - 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토
- 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많음
- 하지만 코딩 테스트에서의 대부분의 그리디 문제는 **탐욕법으로 얻은 해가 최적이 되는 상황에서, 이를 추론**할 수 있어야 풀리도록 출제



## Implementation

#### 구현(Implementation) <small> 시뮬레이션과 완전 탐색</small>

- **머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정**

- 구현 유형의 문제 =  **풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제**

- 구현 유형의 예시

  - 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
  - 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
  - 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제 <small><파이썬 강점> </small>
  - 적절한 라이브러리를 찾아서 사용해야 하는 문제 <small> ex) 순열과 조합 </small>

- 일반적으로 알고리즘 문제에서의 2차원 공간은 **행렬(Matrix)**의 의미

  - x, y의 2차원 좌표계와는 달리 왼쪽 위에서 (0,0)이 시작

- 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 **방향 백터**가 자주 활용

  ```python
  # 동, 북, 서, 남
  dx = [0, -1, 0, 1]	# 행(가로)
  dy = [1, 0, -1, 0]	# 열(세로)
  
  # 현재 위치
  x, y = 2, 2
  
  for i in range(4):
      # 다음 위치
      nx = x + dx[i]
      ny = y + dy[i]
      print(nx, ny)
  ```



## DFS/BFS

#### 그래프 탐색 알고리즘: DFS/BFS

- 탐색(Search)이란 많은 양의 데이터 중에서 **원하는 데이터를 찾는 과정**
- 대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있음
- **DFS/BFS는 코딩 테스트에서 매우 자주 등장하는 유형**이므로 반드시 숙지

#### 스택 자료구조

- 먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)의 자료구조

- **입구와 출구가 동일한 형태**로 스택을 시각화할 수 있음

  - 박스 쌓기 예시

- **스택 구현 예제 (Python)**

  ```python
  stack = [] 
  
  # 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
  stack.append(5)
  stack.append(2)
  stack.append(3)
  stack.append(7)
  stack.pop()
  stack.append(1)
  stack.append(4)
  stack.pop()
  
  print(stack[::-1])	# 최상단 원소(top)부터 출력	[1, 3, 2, 5]
  print(stack)		# 최하단 원소부터 출력	[5, 2, 3, 1]
  ```

- **스택 구현 예제 (Java)**

  ```java
  import java.util.*;
  
  public class Main{
      public static void main(String[] args){
          Stack<Integer> s = new Stack<>();
          
          s.push(5);
      	s.push(2);
     	 	s.push(3);
      	s.push(7);
      	s.pop();
      	s.push(1);
      	s.push(4);
      	s.pop();
          
          // 스택의 최상단 원소부터 출력
          while(!s.empty()){
              System.out.print(s.peek() + " ");	// 실행 결과: 1 3 2 5
              s.pop();
          }
      }
  }
  ```

#### 큐 자료구조

- 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
- 큐는 **입구와 출구가 모두 뚫려 있는 터널**과 같은 형태로 시각화 할 수 있음

- **큐 구현 예제 (Python)**

  ```python
  from collections import deque
  
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용 (시간적 우수)
  queue = deque()
  
  # 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
  # 오른쪽에서 들어와서 왼쪽으로 나가는 반대 구조
  queue.append(5)
  queue.append(2)
  queue.append(3)
  queue.append(7)
  queue.popleft()
  queue.append(1)
  queue.append(4)
  queue.popleft()
  
  print(queue)	# 먼저 들어온 순서대로 출력 	deque([3, 7, 1, 4])
  queue.reverse()	# 역순으로 바꾸기
  print(queue)	# 나중에 들어온 원소부터 출력 	deque([4, 1, 7, 3])
  ```

- **큐 구현 예제 (Java)**

  ```java
  import java.util.*;
  
  public class Main{
      public static void main(String[] args){
          Queue<Integer> q = new LinkedList<>();
          
          q.offer(5);
          q.offer(2);
          q.offer(3);
          q.offer(7);
          q.poll();
          q.offer(1);
          q.offer(4);
          q.poll();
          
          // 먼저 들어온 원소부터 추출
          while(!q.isEmpty()){
              System.out.print(q.poll() + " ");	// 실행 결과: 3 7 1 4
          }
      }
  }
  ```

#### 재귀 함수

- 재귀 함수(Recursive Function)란 **자기 자신을 다시 호출**하는 함수

- 단순한 형태의 재귀 함수 예제

  - '재귀 함수를 호출합니다.' 라는 문자열을 무한히 출력
  - 어느정도 출력하다가 최대 재귀 깊이 초과 메시지가 출력

  ```python
  def recursive_function():
      print('재귀 함수를  호출합니다.')
      recursive_function()
      
  recursive_function()
  ```

- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 함

- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있음

  ```python
  def recursive_function():
      # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
      if i == 100:
          return
      print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
      recursive_function(i+1)
      print(i, '번째 재귀함수를 종료합니다.')
      
  recursive_function()
  ```

- **팩토리얼 구현 예제**

  - n! = 1 x 2 x 3 x ... x (n-1) x n
  - 수학적으로 0!과 1!의 값은 1임

  ```python
  # 반복적으로 구현한 n!
  def factorial_iterative(n):        
      result = 1
      # 1부터 n까지의 수를 차례대로 곱하기
      for i in range(1, n + 1):
         result *= i
      return result
  
  # 재귀적으로 구현한 n!
  def factorial_recursive(n):        
      if n <= 1: # n이 1 이하인 경우 1을 반환
          return 1
      # n! = n * (n - 1)!를 그대로 코드로 작성하기
      return n * factorial_recursive(n - 1)
  
  # 각각의 방식으로 구현한 n! 출력(n = 5)
  print('반복적으로 구현:', factorial_iterative(5))
  print('재귀적으로 구현:', factorial_recursive(5))
  ```

- 최대공약수 계산(유클리드 호제법) 예제

  - <u>두 개의 자연수에 대한 최대공약수</u>를 구하는 대표적인 알고리즘

  - **유클리드 호제법**

    - 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 합시다.
    - 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같습니다.

    ```python
    def gcd(a, b):
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)
        
    print(gcd(192, 162))
    ```

  - 유클리드 호제법의 아이디어를 그대로 재귀 함수로 작성할 수 있음

    - **예시**: GCD(192, 162)

      | 단계 |  A   |  B   |
      | :--: | :--: | :--: |
      |  1   | 192  | 162  |
      |  2   | 162  |  30  |
      |  3   |  30  |  12  |
      |  4   |  12  |  6   |

- **재귀 함수 사용의 유의 사항**

  - 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있음
    - 단, 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수 있으므로 신중하게 사용
  - 모든 <u>재귀 함수는 반복문을 이용하여 동일한 기능을 구현</u>할 수 있음
  - 재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있음
  - 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓임
    - 그래서 스택을 사용해야할 때 구현상 **스택 라이브러리 대신에 재귀 함수를 이용**하는 경우가 많음

#### DFS (Depth-First Search)

- DFS는 **깊이 우선 탐색**이라고 부르며 그래프에서 **깊은 부분을 우선적으로 탐색하는 알고리즘**
- DFS는 **스택 자료구조(혹은 재귀함수)를 이용**하며, 구체적인 동작 과정은 다음과 같음
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.
  2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리합니다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.
  
![image-20201015001153248](https://user-images.githubusercontent.com/45402031/96075853-ee681e80-0ee6-11eb-9602-3bf16cfbe937.png)

- **DFS 소스코드 예제 (Python)**

  ```python
  # DFS 메서드 정의
  def dfs(graph, v, visited):
      # 현재 노드를 방문 처리
      visited[v] =  True
      print(v, end = ' ')
      # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
      for i in graph[v]:
          if not visited[i]:
              dfs(graph, i, visited)	
  
  # 각 노드가 연결된 정보를 표현 (2차원 리스트)
  graph = [
      [],
      [2, 3, 8],
      [1, 7],
      [1, 4, 5],
      [3, 5],
      [3, 4],
      [7],
      [2, 6, 8],
      [1, 7]
  ]
  
  # 각 노드가 방문된 정보를 표현 (1차원 리스트)
  visited = [False] * 9
  
  # 정의된 DFS 함수 호출
  dfs(graph, 1, visited)
  ```
  

- DFS 소스코드 예제 (Java)

  ```java
  import java.util.*;
  
  public class Main{
      public static boolean[] visited = new boolean[9];
      public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
      
      // DFS 함수 정의
      public static void dfs(int x){
          // 현재 노드를 방문 처리
          visited[x] = true;
          System.out.print(x + " ");
          // 현재 노드와 연결돤 다른 노드를 재귀적으로 방문
          for(int i = 0; i < graph.get(x).size(); i++){
              int y = graph.get(x).get(i);
              if(!visited[y]) dfs(y);
          }
      }
      
      public static void main(String[] args){
          /*
          그래프 연결된 내용 생략
          */
          // dfs(1)
      }
  }
  ```

#### BFS (Breadth-First Search)

- BFS는 **너비 우선 탐색**이라고도 부르며, 그래프에서 **가까운 노드부터 우선적으로 탐색하는 알고리즘**
- BFS는 **큐 자료구조**를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 합니다.
  2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리합니다.
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.  

- 특정 조건에서의 **최단경로 문제**를 해결하기 위해 효과적으로 사용될 수 있음

![image-20201015002844846](https://user-images.githubusercontent.com/45402031/96076011-561e6980-0ee7-11eb-8aa1-5041f309a272.png)

- **BFS 소스코드 예제 (Python)**

  ```python
  from collections import deque
  
  # BFS 메서드 정의
  def bfs(graph, start, visited):
      # 큐(Queue) 구현을 위해 deque 라이브러리 사용
      queue = deque([start])
      # 현재 노드를 방문 처리
      visited[start] = True
      # 큐가 빌 때까지 반복
      while queue:
          # 큐에서 하나의 원소를 뽑아 출력하기
          v =  queue.popleft()
          print(v, end = ' ')
          # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
          for i in graph[v]:
              if not visited[i]:
                  queue.append(i)
                  visited[i] = True
                  
  # 각 노드가 연결된 정보를 표현 (2차원 리스트)
  graph = [
      [],
      [2, 3, 8],
      [1, 7],
      [1, 4, 5],
      [3, 5],
      [3, 4],
      [7],
      [2, 6, 8],
      [1, 7]
  ]
  
  # 각 노드가 방문된 정보를 표현 (1차원 리스트)
  visited = [False] * 9
  
  # 정의된 BFS 함수 호출
  bfs(graph, 1, visited)  
  ```

- **BFS 소스코드 예제 (Java)**

  ```java
  import java.util.*;
  
  public class Main{
      public static boolean[] visited = new boolean[9];
      public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
      
      // BFS 함수 정의
      public static void bfs(int start){
          Queue<Integer> q = new LinkedList<>();
          q.offer(start);
          // 현재 노드를 방문 처리
          visited[start] = true;
          // 큐가 빌 때까지 반복
          while(!q.isEmpty()){
              // 큐에서 하나의 원소를 뽑아 출력
              int x = q.poll();
              System.out.print(x + " ");
              // 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
              for(int i = 0; i > graph.get(x).size(); i++){
              	int y = graph.get(x).get(i);
                  if(!visited[y]){
                      q.offer(y);
                      visited[y] = true
                  }
              }
          }
      }
      
     // 메인 함수 생략
  }
  ```
