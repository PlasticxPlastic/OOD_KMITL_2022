    
class range():
    def __init__(self, n , m = 0 ,p = 1):
        if(m==0 and p==1):
            self.start = float(m)
        else:
            self.start = float(n)
        if(m==0):
            self.end = float(n)
        else:
            self.end = float(m)
        self.step = float(p)
        self.l = []

    def fnc(self):
        start = self.start
        end = self.end
        step = self.step
        l = self.l

        while(start < end):
            temp = start
            temp = round(temp,3)
            l.append(temp)
            start += step

        return l

    
    def __str__(self) -> str:
        return '{self.l}'.format(self = self)
    

print("*** New Range ***")
inp = list(input('Enter Input : ').split())
if len(inp)==3:
    x,y,z = inp[0],inp[1],inp[2]
elif len(inp)==2:
    x,y = inp[0],inp[1]
    z = 1
elif len(inp)==1:
    x = inp[0]
    y = 0
    z = 1
R1 = range(x,y,z)
u = R1.fnc()
k = [float(x) for x in u]
print('(',end='')
print(*k,sep=', ',end='')
print(')',end='')

