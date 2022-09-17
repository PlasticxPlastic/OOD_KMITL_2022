class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = self.tail = Node('|')
        self.size = 1

    def isEmpty(self):
        return self.size == 0

    def __str__(self):
        x, s = self.head, str(self.head.data) + " "
        while x.next is not None:
            s += str(x.next.data) + " "
            x = x.next
        return s

    def L(self):
        x = self.head
        if x.data == '|':
            return
        while x.next.data != '|':
            x = x.next
        cursor = x.next
        if x.prev != None:
            x.prev.next = cursor
        x.next = cursor.next
        cursor.next = x
        cursor.prev = x.prev
        if x.prev != None:
            x.prev = cursor
        if x.next == None:
            self.tail = x
        if cursor.prev == None:
            self.head = cursor

    def R(self):
        x = self.head
        if self.tail.data == '|':
            return
        while x.data != '|':
            x = x.next
        cursor = x.next
        if x.prev != None:
            x.prev.next = cursor
        else:
            self.head = cursor
        x.next = cursor.next
        if x.next != None:
            cursor.next.prev = x
        else:
            self.tail = x
        cursor.next = x
        cursor.prev = x.prev
        x.prev = cursor

    def D(self):
        if self.tail.data == "|" or self.size < 2:
            return
        x = self.head
        while x.data != "|":
            x = x.next
        cursor = x.next
        x.next = cursor.next
        if cursor.next != None:
            cursor.next.prev = x
        else:
            self.tail = x

    def B(self):
        if self.head.data == "|":
            return
        x = self.head
        while x.next.data != "|":
            x = x.next
        cursor = x.next
        cursor.prev = x.prev
        if x.prev != None:
            cursor.prev.next = cursor
        else:
            self.head = cursor

    def I(self,data):
        newNode = Node(data)
        self.size += 1

        x = self.head
        while x.data != "|":
            x = x.next
        newNode.next = x
        if x.prev != None:
            x.prev.next = newNode
        newNode.prev = x.prev
        if x.prev == None:
            self.head = newNode
        x.prev = newNode


l = LinkedList()
input = input('Enter Input : ').split(',')
for i in input:
    cm = i.split()
    if cm[0] == 'I':
        l.I(cm[1])
    elif cm[0] == 'L':
        l.L()
    elif cm[0] == 'R':
        l.R()
    elif cm[0] == 'B':
        l.B()
    elif cm[0] == 'D':
        l.D()
print(l)
