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

ip, x = input("Enter code,hint : ").split(",")

q = Queue()
value = ord(ip[0]) - ord(x)
if value < 0:
    ascending = True
    value = value * -1
else:
    ascending = False
for i in range(len(ip)):
    if ip[i] != ",":
        if(ascending == True):
            code = chr(ord(ip[i]) + value)
            q.enqueue(code)
            print(q.items)
        else:
            code = chr(ord(ip[i]) - value)
            q.enqueue(code)
            print(q.items)
    else:
        break
