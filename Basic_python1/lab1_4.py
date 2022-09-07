from itertools import count


def f():
    print("*** Fun with Drawing ***")
    a = int(input("Enter input : "))
    size = ((a-1)*2)*2+1
    x = (2*a)-1
    sq = [[0 for i in range(size)]for j in range(size)]
    set_sharp_dot = 0

    for i in range(x):
        for j in range(i,size-i):
            if(set_sharp_dot %2 == 0):
                sq[i][j] = "#"
                sq[size-i-1][j] = "#"
                sq[j][i] = "#"
                sq[j][size-i-1] = "#"
            else:
                sq[i][j] = "."
                sq[size-i-1][j] = "."
                sq[j][i] = "."
                sq[j][size-i-1] = "."
        set_sharp_dot += 1

    for i in range(size):
        for j in range(size): 
            print(sq[i][j],end="")
        print()


            


f()
        
