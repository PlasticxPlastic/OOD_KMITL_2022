class doublyLinkedlist:
    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            if prev is None:
                self.prev = None
            else:
                self.prev = prev
            if next is None:
                self.next = None
            else:
                self.next = next

    def __init__(self):
        self.dummy = self.Node(None, None, None)
        self.dummy.next = self.dummy.prev = self.dummy
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "linked list : "
        s = 'linked list : '
        x = self.dummy.next
        for i in range(self.size - 1):
            s += str(x.data) + '->'
            x = x.next
        s += str(x.data)
        return s

    def str_reverse(self):
        if self.isEmpty():
            return "reverse :"
        s = "reverse : "
        x = self.dummy.next
        x = self.nodePos(self.size - 1)
        for i in range(self.size - 1):
            s += str(x.data) + "->"
            x = x.prev
        s += x.data
        return s

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def addBefore(self, pos, data):
        y = pos.prev
        data = self.Node(data, y, pos)
        y.next = pos.prev = data
        self.size += 1

    def nodePos(self, i):
        p = self.dummy
        for j in range(-1, i):
            p = p.next
        return p

    def insert(self, index, data):
        if 0 <= int(index) <= self.size:
            self.addBefore(self.nodePos(int(index)), data)
            print("index = " + index + " and data = " + data)
            return
        else:
            print("Data cannot be added")
            return

    def append(self, data):
        self.addBefore(self.nodePos(self.size), data)

    def removeNode(self, data):
        if self.isEmpty():
            print("Not Found!")
            return
        y = data.prev
        x = data.next
        y.next = x
        x.prev = y
        self.size -= 1


l = doublyLinkedlist()
inp = input("Enter Input : ")
inp = inp.replace(", ", ",")
inp = inp.split(',')
for data in inp:
    a = data.split()
    if a[0] == 'A':
        l.append(a[1])
    elif a[0] == 'Ab':
        l.addBefore(l.nodePos(0),a[1])
    elif a[0] == 'I':
        index,data = a[1].split(":")
        l.insert(index,data)
    elif a[0] == 'R':
        q = False
        for i in range(l.size):
            if int(l.nodePos(i).data) == int(a[1]):
                print(f"removed : {l.nodePos(i).data} from index : {i}")
                l.removeNode(l.nodePos(i))
                q = True
                break
        if q is False:
            print("Not Found!")
    print(l)
    print(l.str_reverse())


