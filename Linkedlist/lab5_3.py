class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return
        s = ''
        p = self.head
        for i in range(self.size-1):
            s += str(p.data)+ ' '
            p = p.next
        s += str(p.data)
        return s

    def str_reverse(self):
        if self.isEmpty():
            return
        s = ''
        p = self.tail
        for i in range(self.size-1):
            s += str(p.data) + ' '
            p = p.previous
        s += str(p.data)
        return s

    def isEmpty(self):
        return self.size == 0

    def append(self,data):
        newNode = node(data)
        newNode.next = None
        if self.head == None:
            newNode.previous = None
            self.head = self.tail = newNode
            self.size+=1
        else:
            x = self.head
            while x.next != None:
                x = x.next
            x.next = newNode
            self.tail = newNode
            newNode.previous = x
            self.size += 1

input =input("Enter Input (L1,L2) : ").split()
L1 =str(input[0]).split("->")
L2 =str(input[1]).split("->")
link1 = linkedlist()
link2 = linkedlist()
for i in L1:
    link1.append(i)
for i in L2:
    link2.append(i)
print("L1    : ",end="")
print(link1)
print("L2    : ",end="")
print(link2)
print("Merge : ",end="")
print(link1,end=" ")
print(link2.str_reverse())