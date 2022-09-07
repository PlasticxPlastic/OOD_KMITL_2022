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


def ManageStack(ip, s):
    if len(ip) > 1:
        ip,vl = ip.split()
    if ip[0] == 'A':
        s.push(vl)
        print(f"Add = {vl}")
    elif ip[0] == 'P':
        if not s.isEmpty():
            print("Pop = {}".format(s.peek()))
            s.pop()
        else:
            print("-1")
    elif ip[0] == 'D':
        if not s.isEmpty():
            templ = s.items.copy()
            for e in range(len(templ)):
                if templ[e] == vl:
                    print("Delete = " + vl)
                    s.items.remove(vl)
        else:
            print("-1")
    elif ip[0] == 'L' and ip[1] == 'D':
        dl = []
        if not s.isEmpty():
            templ = s.items.copy()
            ua = None
            for e in range(len(templ)):
                if int(templ[e]) < int(vl):
                    s.items.remove(templ[e])
                    deleted = templ[e]
                    if deleted != 0:
                        if deleted != ua:
                            dl.append(int(deleted))
                            ua = deleted
            for g in range(len(dl)):
                dl.sort()
                print("Delete = {} Because {} is less than {}".format(dl[g], dl[g], vl))
        else:
            print("-1")
    elif ip[0] == 'M' and ip[1] == 'D':
        dl = []
        if not s.isEmpty():
            ua = None
            templ = s.items.copy()
            for e in range(len(templ)):
                if int(templ[e]) > int(vl):
                    s.items.remove(templ[e])
                    deleted = templ[e]
                    if deleted != 0:
                        if deleted != ua:
                            ua = deleted
                            dl.append(int(deleted))
                            dl.sort()
            for g in range(len(dl)):
                print("Delete = {} Because {} is more than {}".format(dl[g], dl[g], vl))
        else:
            print("-1")
ip = [e for e in input("Enter Input : ").split(',')]
s = Stack()
for x in ip:
    ManageStack(x,s)
if not s.isEmpty():
    print("Value in Stack = [", end='')
    for i in range(len(s.items)):
        if i != len(s.items)-1:
            print(s.items[i],end=', ')
        else:
            print(s.items[i],end=']')
else:
    print("Value in Stack = ", end='')
    print(s.items)