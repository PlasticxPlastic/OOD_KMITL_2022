print(" *** Stack implement by Python list***")
class Stack:
    def __init__(self, ls=None):
        self.items = []
        self.size = len(self.items)

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


ls = [e for e in input("Enter data to stack : ").split()]

s = Stack(ls)

for e in ls:
    s.push(e)

print(s.size, "Data in stack : ", s.items)

while not s.isEmpty():
    s.pop()

print(s.size, "Data in stack : ", s.items)
