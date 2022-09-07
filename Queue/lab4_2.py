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


ip = input("Enter people : ")

mline = Queue()
cs1line = Queue()
cs2line = Queue()
minutecs1 = 0
minutecs2 = 0
for e in ip:
    mline.enqueue(e)
for i in range(len(ip)):
    if minutecs1 >1 and minutecs1%3 == 0 and not cs1line.isEmpty():
        cs1line.dequeue()
    if minutecs2 >1 and minutecs2%2 == 0 and not cs2line.isEmpty():
        cs2line.dequeue()
    if cs1line.size() < 5:
        customer = mline.front()
        mline.dequeue()
        cs1line.enqueue(customer)
    elif cs2line.size() < 5:
        customer = mline.front()
        mline.dequeue()
        cs2line.enqueue(customer)
    if not cs1line.isEmpty():
        minutecs1 += 1
    if not cs2line.isEmpty():
        minutecs2 += 1
    print(i+1,end=" ")
    print(mline.items,end=" ")
    print(cs1line.items,end=" ")
    print(cs2line.items)
