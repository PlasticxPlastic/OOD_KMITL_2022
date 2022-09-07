class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enqueue(self, i):
        self.items.append(i)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    def front(self):
        return self.items[0]


ip = [e for e in input("Enter Input : ").split(',')]

q = Queue()
for i in range(len(ip)):
    if len(ip[i]) != 1:
        value, dq = ip[i].split()
    else:
        value = ip[i]
    if value == 'E':
        q.enqueue(dq)
        print("Add %d index is %d"%(int(dq), len(q.items)-1))
    elif value == 'D':
        if not q.isEmpty():
            dq = q.front()
            q.dequeue()
            print("Pop %d size in queue is %d" % (int(dq), len(q.items)))
        else:
            print("-1")

if q.isEmpty():
    print("Empty")
else:
    print("Number in Queue is :  ",end="")
    print(q.items)
