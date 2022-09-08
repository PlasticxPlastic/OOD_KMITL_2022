#รถไฟอยู่ขบวนหนึ่ง โดยรถไฟนั้นจะมีหมายเลขกำกับตู้แต่ละตู้อยู่และรถไฟก็มีหัวรถจักรอยู่

#แต่หัวรถจักรดันไปต่อกับตู้รถไฟอยู่ พี่ต้องการให้น้อง ๆ ทำการแบ่งขบวนรถไฟออก

#โดยให้หัวรถจักรอยู่ข้างหน้าสุด และส่วนตู้ที่เหลือให้ทำการต่อกับตู้สุดท้ายโดยไม่มีการเปลี่ยนลำดับของตู้

#ซึ่งพี่จะให้หมายเลข 0 แทนเป็นหัวรถจักร ส่วน หมายเลขอื่นจะเป็นตู้รถไฟ

#เช่น 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6

#เป็น 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1 ( ให้ใช้ singly linked list)

class LinkedList:
    def __init__(self, head=None):
        if head is None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = last = head
            tail = head.next
            self.size = 1
            while tail is not None:
                last = tail
                tail = tail.next
                self.size += 1
            self.tail = last

    def __str__(self):
        if self.isEmpty():
            return ""
        else:
            ret = []
            tail = self.head
            while tail != None:
                ret.append(str(tail.value))
                tail = tail.next
            return " <- ".join(ret)

    def append(self, value):
        # check value
        if type(value) != ListNode:
            node = ListNode(value)
        else:
            node = value

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def isEmpty(self):
        return self.size == 0


class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None

print(" *** Locomotive ***")
input = input("Enter Input : ").split()

ft = False
f_train = LinkedList()
r_train = LinkedList()
#print before
print("Before : ",end="")
for i in range(len(input)):
    if i != len(input) - 1:
        print(input[i] + " <- ",end="")
    else:
        print(input[i])
# find locomotive
for i in input:
    if i == "0":
        ft = True
    if ft:
        f_train.append(i)
    else:
        r_train.append(i)

print("After : ",end="")
if not r_train.isEmpty():
    print(f_train,end=" <- ")
    print(r_train)
else:
    print(f_train)

