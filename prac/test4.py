class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enQ(self,data):
        self.items.append(data)

    def deQ(self):
        return self.items.pop(0)

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        node = self.root
        while True:
            if data < node.left.data:
                if node.left is None:
                    node.left = Node(data)
                    return self.root
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(data)
                    return self.root
                node = node.right

    def printTree(self,node,level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level,node.data)
            self.printTree(node.left, level+1)

    def Preorder(self,node):
        if node is None:
            return ''
        s = str(node.data) + ' ' \
            + self.Preorder(node.left) \
            + self.Preorder(node.right)
        return s

    def Inorder(self,node):
        if node is None:
            return ''
        s = self.Inorder(node.left) \
            + str(node.data) + ' '\
            + self.Inorder(node.right)
        return s

    def Postorder(self,node):
        if node is None:
            return ''
        s = self.Postorder(node.left) \
            + self.Postorder(node.right) \
            + str(node.data) + ' '
        return s

    def BFS(self):
        q = Queue()
        q.enQ(self.root)
        s = 'Level order : '
        while not q.isEmpty():
            node = q.deQ()
            s += str(node.data) + ' '
            if node.left is not None:
                q.enQ(node.left)
            if node.right is not None:
                q.enQ(node.right)
        return s

T = BST()
inp = [i for i in input('Enter input : ').split()]
s = Stack()
operand = ['*', '+', '-', '/']
for i in inp:
    if i not in operand:
        n = Node(i)
        s.push(n)
    else:
        n = Node(i)
        n.right = s.pop()
        n.left = s.pop()
        s.push(n)
T.insert(n)
T.printTree(n)


