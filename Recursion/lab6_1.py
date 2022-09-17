def Max(lip):
    if len(lip) == 1:
        return lip[0]
    else:
        m = Max(lip[1:])
        if int(m) > int(lip[0]):
            return m
        else:
            return lip[0]


ip = list(input('Enter Input : ').split())
x = Max(ip)
print("Max : ",end="")
print(x)