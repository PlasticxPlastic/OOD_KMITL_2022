class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None
        self.height = 1

class AVL(object):
    def __init__(self):
        self.root = None

    def getHeight(self,root):
        if not root:
            return 0
        return root.height
    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    def left_rotate(self,z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y
    def right_rotate(self,z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def insert(self,node,data):
        if not node:
            node = Node(data)
            return node
        elif data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right,data)

        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))
        balance = self.getBalance(node)
        if balance > 1 and data < node.left.data:
            print("not balance")
            return self.right_rotate(node)
        if balance < -1 and data >= node.right.data:
            print("not balance")
            return self.left_rotate(node)
        if balance > 1 and data >= node.left.data:
            print("not balance")
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and data < node.right.data:
            print("not balance")
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def printTree(self,node,level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level , node.data)
            self.printTree(node.left, level + 1)

myTree = AVL()
inp = input('Enter Input : ').split()
for data in inp:
    print(f'insert : {data}')
    myTree.root = myTree.insert(myTree.root, int(data))
    myTree.printTree(myTree.root)
    print('===============')