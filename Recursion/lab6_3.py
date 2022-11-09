a, b = input('Enter Input a b : ').split(' ')
a = int(a)
b = int(b)


def POW(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    return a * POW(a, b - 1)


print(POW(a, b))
