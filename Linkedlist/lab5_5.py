class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


def createLL(LL):
    head = Node(LL[0])
    temp = head
    for i in range(1, len(LL)):
        newNode = Node(LL[i])
        temp.next = newNode
        temp = newNode
    return head


def printLL(head):
    cur = head
    s = ""
    while cur is not None:
        s += str(cur)
        s += " "
        cur = cur.next
    return s


def SIZE(head):
    size = 1
    temp = head
    while temp.next is not None:
        size += 1
        temp = temp.next
    return size


def scarmble(head, b, r, size):
    cutSize = size
    cutSize *= b / 100
    cutSize = int(cutSize)
    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = head
    temp = head
    i = 0
    while i < cutSize:
        if i == cutSize - 1:
            head = temp.next
            temp.next = None
        temp = temp.next
        i += 1
    print('BottomUp {0:.3f} % : '.format(b) + '{0}'.format(printLL(head)))

    cutSize = size
    cutSize *= r / 100
    cutSize = int(cutSize)
    newTail = False
    oldHead = head
    newHead = head
    temp = oldHead
    i = 0
    while i < cutSize:
        if i == cutSize - 1:
            newHead = temp.next
            temp.next = None
        temp = temp.next
        i += 1
    s = 0
    if SIZE(oldHead) < SIZE(newHead):
        s = SIZE(oldHead)
        newTail = True
    else:
        s = SIZE(newHead)
    i = 0
    temp = oldHead
    newTemp = newHead
    while i < s:
        tempNext = temp.next
        newTempNext = newTemp.next
        if temp.next is not None and newTemp.next is not None:
            tempNext = temp.next
            temp.next = newTemp
            newTempNext = newTemp.next
            newTemp.next = tempNext
            newTemp = newTempNext
        elif temp.next is not None and newTemp.next is None:
            tempNext = temp.next
            temp.next = newTemp
            newTemp.next = tempNext
        elif temp.next is None and newTemp.next is not None:
            temp.next = newTemp
        elif temp.next is None and newTemp.next is None:
            temp.next = newTemp
        temp = tempNext
        newTemp = newTempNext
        i += 1
    head = oldHead
    print('Riffle {0:.3f} % : '.format(r) + '{0}'.format(printLL(head)))

    cutSize = s
    i = 0
    if newTail:
        temp = head
        while i < (2 * cutSize) - 1:
            if i == (2 * cutSize) - 2:
                oldTail = temp
            temp = temp.next
            i += 1
        i = 0
        oldTailnext = oldTail.next
        temp = head
        while i < cutSize - 1:
            oldTail.next = temp.next
            oldTail = temp.next
            temp.next = temp.next.next
            oldTail.next = None
            temp = temp.next
            i += 1
        oldTail.next = oldTailnext
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        tail = temp
        temp = head
        while i < cutSize:
            tail.next = temp.next
            tail = tail.next
            temp.next = temp.next.next
            tail.next = None
            temp = temp.next
            i += 1
    print('Deriffle {0:.3f} % : '.format(r) + '{0}'.format(printLL(head)))

    cutSize = size
    cutSize *= b / 100
    cutSize = size - int(cutSize)
    tail = head
    i = 0
    while tail.next is not None:
        tail = tail.next
    tail.next = head
    temp = head
    while i < cutSize:
        if i == cutSize - 1:
            head = temp.next
            temp.next = None
        temp = temp.next
        i += 1
    print('Debottomup {0:.3f} % : '.format(b) + '{0}'.format(printLL(head)))


inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)
