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

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        node = self.root
        while True:
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                    return self.root
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(data)
                    return self.root
                node = node.right

    def Preorder(self,node):
        if node is None:
            return ''

        s = str(node.data) + ' ' \
            +self.Preorder(node.left) \
            +self.Preorder(node.right)
        return s

    def BFS(self):
        q = Queue()
        q.enQ(self.root)
        s = 'level order : '
        while not q.isEmpty():
            node = q.deQ()
            s += str(node.data) + ' '
            if node.left is not None:
                q.enQ(node.left)
            if node.right is not None:
                q.enQ(node.right)
        return s

T = BST()
print(' *** Binary Search Tree ***')
inp = [int(item) for item in input("Enter Input : ").split()]
for i in inp:
    root = T.insert(i)
print()
print(' --- Tree traversal ---')
print(T.BFS())
print("Preorder : {0}".format(T.Preorder(T.root)))
