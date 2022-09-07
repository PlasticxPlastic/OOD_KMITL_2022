class StackCalc:
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

    def run(self,arg):
        listarg = arg.split()
        def isnum(s):
            try:
                int(s)
                return True
            except:
                return False
        for i in listarg:
            if isnum(i):
                self.push(i)
            else:
                if len(i) == 1:
                    if i == "+":
                        x = float(self.pop())
                        y = float(self.pop())
                        z = y + x
                        self.push(z)
                    elif i == "-":
                        x = float(self.pop())
                        y = float(self.pop())
                        z = x - y
                        self.push(z)
                    elif i == "*":
                        x = float(self.pop())
                        y = float(self.pop())
                        z = y * x
                        self.push(z)
                    elif i == "/":
                        x = float(self.pop())
                        y = float(self.pop())
                        z = x / y
                        self.push(z)
                    else:
                        self.error = True
                        self.value = i
                        break
                elif i[0] == "P" and i[1] == "O" and i[2] == "P":
                    self.pop()
                elif i[0] == "P" and i[1] == "S" and i[2] == "H":
                    self.push(self.peek())
                elif i[0] == "D" and i[1] == "U" and i[2] == "P":
                    self.push(self.peek())
                else:
                    self.error = True
                    self.value = i
        if self.isEmpty() and self.error == False:
            self.value = 0
        elif not self.isEmpty():
            self.error = False
            self.value = int(self.pop())

    def getValue(self):
        if self.error == True:
            return "Invalid instruction: " + str(self.value)
        else:
            return self.value


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())