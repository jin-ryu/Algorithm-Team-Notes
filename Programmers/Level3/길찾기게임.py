
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
import sys 
sys.setrecursionlimit(10**6)    # 재귀 범위 늘려줌

class Tree:
    def __init__(self, info):
        self.data = max(info, key=lambda x:x[1])
        leftList = list(filter(lambda x:x[0]<self.data[0], info))
        rightList = list(filter(lambda x:x[0]>self.data[0], info))

        # 재귀적으로 tree 완성
        if leftList:
            self.left = Tree(leftList)
        else:
            self.left = None

        if rightList:
            self.right = Tree(rightList)
        else:
            self.right = None


def traverse(node, postList, preList):
    preList.append(node.data)   # 전위 순회

    if node.left is not None:
        traverse(node.left, postList, preList)

    if node.right is not None:
        traverse(node.right, postList, preList)

    postList.append(node.data)  # 후위 순회


def solution(nodeinfo):
    answer = []
    postList = []
    preList = []

    root = Tree(nodeinfo)
    traverse(root, postList, preList)

    # 좌표를 노드 번호로 변환
    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, preList)))
    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, postList)))

    return answer