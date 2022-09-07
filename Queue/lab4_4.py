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


IDemp, CM = input("Enter Input : ").split("/")
IDemp = IDemp.split(",")
CM = CM.split(",")

data_id = {}

for e in IDemp:
    department, id = e.split()
    if department not in data_id:
        data_id[department] = []
    data_id[department].append(id)

tl = {}

for command in CM:
    if len(command) > 1:
        cm, id_q = command.split()
        for i in data_id:
            if id_q in data_id[i]:
                if i not in tl:
                    tl[i] = Queue()
                tl[i].enqueue(id_q)
    else:
        temp = tl.copy()
        x = 0
        for dp in temp:
            if tl[dp].isEmpty():
                continue
            else:
                dq = tl[dp].dequeue()
                x = 1
                print(dq)
                break
        for dp in temp:
            if tl[dp].isEmpty():
                del tl[dp]
        if x == 0:
            print("Empty")