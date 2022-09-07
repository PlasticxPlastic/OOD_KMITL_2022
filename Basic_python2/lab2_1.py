class Calculator :

    ### Enter Your Code Here ###
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self):
        return self.x + self.y
    def __sub__(self):
        return self.x-self.y
    def __mul__(self):
        return self.x * self.y
    def __truediv__(self):
        return self.x / self.y
x,y = input("Enter num1 num2 : ").split(",")
C1 = Calculator(int(x),int(y))
print(C1.__add__())
print(C1.__sub__())
print(C1.__mul__())
print(C1.__truediv__())