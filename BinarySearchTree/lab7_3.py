class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None
        self.min = 0
        self.max = 0

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        node = self.root
        while True:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                    return self.root
                node = node.left
            else:
                if node.right == None:
                    node.right = Node(data)
                    return self.root
                node = node.right

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def less_thanx(self, node, data):
        if node == None:
            return 0

        n = self.less_thanx(node.left, data)
        if node.data > data:
            return n
        n += self.less_thanx(node.right, data)

        if node.data <= data:
            n += 1
        return n


T = BST()
inp, k = input('Enter Input : ').split('/')
inp = [int(i) for i in inp.split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print(T.less_thanx(root, int(k)))