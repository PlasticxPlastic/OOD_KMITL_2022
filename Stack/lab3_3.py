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

    def peek(self):
        return self.items[-1]

def postFixeval(st):
    def isnum(s):
        try:
            int(s)
            return True
        except:
            return False
    s = Stack()
    for i in st:
        if isnum(i):
            s.push(i)
        else:
            x = float(s.pop())
            y = float(s.pop())
            if i == "+":
                z = y + x
            elif i == "-":
                z = y - x
            elif i == "*":
                z = y * x
            elif i == "/":
                z = y / x
            s.push(z)
    return s.pop()

print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())

print("Answer : ",'{:.2f}'.format(postFixeval(token)))