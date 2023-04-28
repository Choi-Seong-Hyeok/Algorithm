import sys
input = sys.stdin.readline
'''
트리순회 : inorder, preorde, postorder 
해야할것들 
    1. 각 노드의 root , left , right를 나타내야함 --> class 사용 
    2. 순회들의 함수를 만들어줘야함 함수 안에서 표현을 잘해야함. --> 객체를 참조하는 것인지 당시 루트값을 나타내고 싶은것인지.
    3. dictionary 형태로 class를 넣어줘야함.
'''
n = int(input())
node = [int(input().split()) for _ in range(n)]

class Node():
    def __init__(self,root,left,right):
        self.root = root
        self.left = left
        self.right = right

def preorder(node):
    print(node.root,end = ' ')
    if node.left != '.':
        preorder(node_dic[node.left])
    if node.right != '.':
        preorder(node_dic[node.right])

def inorder(node):
    if node.left != '.':
        inorder(node_dic[node.left])
    print(node.root,end=' ')
    if node.right != '.':
        inorder(node_dic[node.right])

def postorder(node):
    if node.left != '.':
        postorder(node_dic[node.left])
    if node.right != '.':
        postorder(node_dic[node.right])
    print(node.root,end=' ')

    




node_dic = {}

for root,left,right in node:
    node_dic[root] = Node(root,left,right)


preorder(node_dic['A'])
print()
