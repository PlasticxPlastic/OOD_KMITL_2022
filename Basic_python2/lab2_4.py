
def f():
    l = list(map(int, input ("Enter Your List : ").split()))
    list_count = len(l)
    l_rst = []
    l_clt = []
    slt = 0
    i = 0
    j = 0
    k = 0
    ans = 0
    if(list_count >= 3):
        while(i<list_count-1):
            i+=1
            j=0
            k=0
            while(j<list_count-1):
                j+=1
                k=0
                while(k<list_count-1):
                    if(i != j and i != k and j != k):
                        test = l[i] + l[j] + l[k]
                        if(test == slt):
                            l_clt.append(l[i])
                            if(k > j):
                                l_clt.append(l[j])
                                l_clt.append(l[k])
                            elif(j > k):
                                l_clt.append(l[k])
                                l_clt.append(l[j])
                            stk1 = l[i]
                            stk2 = l[j]
                            stk3 = l[k]
                            l.remove(stk1)
                            l.remove(stk2)
                            l.remove(stk3)
                            i = 0
                            j = 0
                            k = 0
                            list_count = len(l)
                            if(ans == 0):
                                previousstk = stk1
                            if(previousstk != stk1 or ans == 0):
                                ans+=1
                        else:
                            test = 0
                    k+=1
        p = 0
        for f in range(ans):
            ltemp = [l_clt[p],l_clt[p+1],l_clt[p+2]]
            stu1 = l_clt[p]
            stu2 = l_clt[p+1]
            stu3 = l_clt[p+2]
            l_clt.remove(stu1)
            l_clt.remove(stu2)
            l_clt.remove(stu3)
            p=0
            l_rst.append(ltemp)

        print(l_rst)
    else:
        print("Array Input Length Must More Than 2")

f()