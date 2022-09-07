class Queue:
    def __init__(self, list=None):
        if list is None:
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


class Stack:
    def __init__(self, ls=None):
        self.ls = ls
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


input = input("Enter Input (Normal, Mirror) : ")
normal_bomb = input.split()[0]
mirror_bomb = input.split()[1]

# reverse
temp_mirror = []
for i in range(len(mirror_bomb)):
    temp_mirror.append(mirror_bomb[len(mirror_bomb)-i-1])

mirror_bomb = temp_mirror

# Mirror Section
ms = Stack()
item_queue = Queue()
count_mirror_crush = 0
for i in mirror_bomb:
    if ms.size < 2:
        ms.push(i)
    else:
        ms.push(i)
        check1 = ms.pop()
        check2 = ms.pop()
        check3 = ms.pop()
        if check1 == check2 == check3:
            item_queue.enqueue(i)
            count_mirror_crush += 1
        else:
            ms.push(check3)
            ms.push(check2)
            ms.push(check1)

# Normal Section
ns = Stack()
nq = Queue()
count_normal_crush = 0
count_normal_crush_interupt = 0
for i in normal_bomb:
    if ns.isEmpty():
        ns.push(i)
    elif ns.size == 1:
        ns.push(i)
    else:
        if ns.peek() == i:
            L = ns.pop()
            if ns.peek() == i:
                ns.push(L)
                if not item_queue.isEmpty():
                    ns.push(item_queue.dequeue())
                    check1 = ns.pop()
                    check2 = ns.pop()
                    check3 = ns.pop()
                    if check1 == check2 == check3:
                        count_normal_crush_interupt += 1
                        ns.push(i)
                    else:
                        ns.push(check3)
                        ns.push(check2)
                        ns.push(check1)
                        ns.push(i)
                else:
                    ns.push(i)
                    check1 = ns.pop()
                    check2 = ns.pop()
                    check3 = ns.pop()
                    if check1 == check2 == check3:
                        count_normal_crush += 1
                    else:
                        ns.push(check3)
                        ns.push(check2)
                        ns.push(check1)

            else:
                ns.push(L)
                ns.push(i)
        else:
            ns.push(i)




# print
print("NORMAL :")
print(ns.size)
if ns.isEmpty():
    print("Empty")
else:
    for i in range(ns.size):
        print(ns.items[ns.size-i-1], end="")
    print()
print(str(count_normal_crush) + " Explosive(s) ! ! ! (NORMAL)")
if count_normal_crush_interupt != 0:
    print("Failed Interrupted " + str(count_normal_crush_interupt) + " Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(ms.size)
if ms.isEmpty():
    print("ytpmE")
else:
    for i in range(ms.size):
        print(ms.items[ms.size - i - 1], end="")
    print()
print("(RORRIM) ! ! ! (s)evisolpxE " + str(count_mirror_crush))
