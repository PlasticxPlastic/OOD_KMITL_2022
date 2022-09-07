class Stack:
    def __init__(self, ls=None):
        self.items = []
        self.size = len(self.items)
        self.error = False
        self.value = 0

    def push(self, i):
        self.items.append(i)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]
def dec2bin(decnum):

    s = Stack()
    t = ""
    while decnum != 0:
        x = decnum%2
        decnum = decnum // 2
        s.push(x)
    while not s.isEmpty():
        t = t + str(s.pop())
    return t




print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))