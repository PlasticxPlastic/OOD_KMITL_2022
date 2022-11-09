def display(n, k):
    print("_"*(n-k),end="")
    print("#"*k,end="")
    print()

def staircase(n,row=0):
    if n != 0:
        if row < n:
            row+=1
            display(n,row)
            staircase(n,row)
        elif n < 0:
            if row < n*(-1):
                display(n*(-1),n*(-1) - row)
                row += 1
                staircase(n, row)
    else:
        print("Not Draw!")

num =int(input("Enter Input : "))
staircase(num)
