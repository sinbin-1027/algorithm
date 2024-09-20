'''
7
3 5 1 2 7 4 -5
'''

# 연결 리스트로 구현하기 위해 data, 좌/우 노드를 연결할 수 있도록 선언
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    # 이진탐색트리에서 관리해야 할 변수는 root 하나 뿐
    # 삽입, 탐색, 삭제 등 모든 연산은 root 에서부터 시작
    def __init__(self):
        self.root = None

    # 삽입 연산
    def insert(self, key):
        # root 가 없다면 그냥 삽입
        if self.root is None:
            self.root = Node(key)
        # 데이터가 있다면, 위치를 찾아야 한다.
        else:
            self._insert(self.root, key)

    # 실제로 삽입할 위치를 찾아서 삽입
    # node: 현재 탐색중인 노드 / key: 삽입하고자 하는 값 
    def _insert(self, node, key):
        # 현재노드보다 작으면 왼쪽을 탐색
        if key < node.key:
            # 왼쪽에 노드가 없다 == 삽입 가능한 위치
            if node.left is None:
                node.left = Node(key)
            # 왼쪽에 노드가 있으면, 해당 노드를 기준으로 다시 탐색
            else:
                self._insert(node.left, key)
        # 현재노드보다 크면 오른쪽을 탐색
        else:
            # 오른쪽에 노드가 없다 == 삽입 가능한 위치
            if node.right is None:
                node.right = Node(key)
            # 오른쪽에 노드가 있으면, 해당 노드를 기준으로 다시 탐색
            else:
                self._insert(node.right, key)

    # 탐색 연산
    def search(self, key):
        return self._search(self.root, key)

    # 재귀적으로 노드를 탐색하는 메서드
    def _search(self, node, key):
        # node is None: 끝까지 내려간 상태 -> 더 이상 내려갈 수 없다
        # node.key == key: 발견함
        if node is None or node.key == key:
            return node
        # 현재 노드보다 작으면, 왼쪽을 추가로 탐색
        if key < node.key:
            return self._search(node.left, key)
        # 현재 노드보다 크다면, 오른쪽을 추가로 탐색
        else:
            return self._search(node.right, key)

    # 중위 순회
    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    # 재귀적으로 중위 순회해주는 메서드
    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)

N = int(input())
arr = list(map(int, input().split()))

bst = BinarySearchTree()

for num in arr:
    bst.insert(num)

print("중위 순회 결과:", end=' ')
bst.inorder_traversal()  # 중위 순회: -5 1 2 3 4 5 7

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")
