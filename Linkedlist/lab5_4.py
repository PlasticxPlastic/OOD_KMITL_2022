#กฤษฎาได้มีไอเดียสุดบรรเจิดคือการสร้างโปรแกรม Text Editor แบบ VIM ขึ้นมาใช้งานเอง โดยโปรแกรมนี้จะมีอยู่แค่ 1 Mode คือ Command Mode (inputของเรานั่นแหละ) โดยจะมีคำสั่งอยู่ 5 แบบ คือ Insert (I) , Left (L) , Right (R) , Backspace (B) และ Delete (D) (โดยความสามารถของคำสั่งต่างๆจะอธิบายด้านล่าง) แต่กฤษฎาไม่มีความสามารถทางด้านการสร้างโปรแกรมเลย กฤษฎาจึงได้มาขอร้องน้องๆที่เรียนอยู่วิศวกรรมคอมพิวเตอร์ ให้ช่วยสร้างโปรแกรม Text Editor ที่กฤษฎาต้องการให้หน่อย โดยผลลัพธ์ให้แสดงออกมาเป็น word ที่เหลืออยู่จาก Command ที่เราใส่ลงไป พร้อมกับตำแหน่งของ Cursor

#***** อธิบาย Input 5 แบบ *****

#1.  I <word > :   เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป

#2.  L              :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

#3.  R             :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร

#4.  B             :   เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

#5.  D             :   เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = self.tail = Node('|')
        self.size = 1

    def isEmpty(self):
        return self.size == 0

    def __str__(self):
        x, s = self.head, str(self.head.data) + " "
        while x.next is not None:
            s += str(x.next.data) + " "
            x = x.next
        return s

    def L(self):
        x = self.head
        if x.data == '|':
            return
        while x.next.data != '|':
            x = x.next
        cursor = x.next
        if x.prev != None:
            x.prev.next = cursor
        x.next = cursor.next
        cursor.next = x
        cursor.prev = x.prev
        if x.prev != None:
            x.prev = cursor
        if x.next == None:
            self.tail = x
        if cursor.prev == None:
            self.head = cursor

    def R(self):
        x = self.head
        if self.tail.data == '|':
            return
        while x.data != '|':
            x = x.next
        cursor = x.next
        if x.prev != None:
            x.prev.next = cursor
        else:
            self.head = cursor
        x.next = cursor.next
        if x.next != None:
            cursor.next.prev = x
        else:
            self.tail = x
        cursor.next = x
        cursor.prev = x.prev
        x.prev = cursor

    def D(self):
        if self.tail.data == "|" or self.size < 2:
            return
        x = self.head
        while x.data != "|":
            x = x.next
        cursor = x.next
        x.next = cursor.next
        if cursor.next != None:
            cursor.next.prev = x
        else:
            self.tail = x

    def B(self):
        if self.head.data == "|":
            return
        x = self.head
        while x.next.data != "|":
            x = x.next
        cursor = x.next
        cursor.prev = x.prev
        if x.prev != None:
            cursor.prev.next = cursor
        else:
            self.head = cursor

    def I(self,data):
        newNode = Node(data)
        self.size += 1

        x = self.head
        while x.data != "|":
            x = x.next
        newNode.next = x
        if x.prev != None:
            x.prev.next = newNode
        newNode.prev = x.prev
        if x.prev == None:
            self.head = newNode
        x.prev = newNode


l = LinkedList()
input = input('Enter Input : ').split(',')
for i in input:
    cm = i.split()
    if cm[0] == 'I':
        l.I(cm[1])
    elif cm[0] == 'L':
        l.L()
    elif cm[0] == 'R':
        l.R()
    elif cm[0] == 'B':
        l.B()
    elif cm[0] == 'D':
        l.D()
print(l)
