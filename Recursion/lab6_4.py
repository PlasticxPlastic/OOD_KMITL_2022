def printPole(n, pole1, pole2, pole3):
    if n != 0:
        if n < len(pole1):
            print(pole1[n], end='  ')
        else:
            print('| ', end=' ')
        if n < len(pole2):
            print(pole2[n], end='  ')
        else:
            print('| ', end=' ')
        if n < len(pole3):
            print(pole3[n], end='  ')
        else:
            print('| ', end=' ')
        print()
        printPole(n - 1, pole1, pole2, pole3)
    return


def move(n,  m, A, B, C):
    if n == 1:
        if A[0] == "A" and C[0] == "B":
            B.append(A.pop())
        elif A[0] == "B" and C[0] == "C":
            C.append(B.pop())
        elif A[0] == "A" and C[0] == "C":
            C.append(A.pop())
        elif A[0] == "C" and C[0] == "B":
            B.append(C.pop())
        elif A[0] == "B" and C[0] == "A":
            A.append(B.pop())
        elif A[0] == "C" and C[0] == "A":
            A.append(C.pop())
        print("move 1 from  %s to %s" % (A[0], C[0]))
        print("|  |  |")
        printPole(m, A, B, C)

        B[0], C[0] = C[0], B[0]
        return A, B, C
    else:
        bb, cc = B.copy(), C.copy()
        bb[0], cc[0] = C[0], B[0]
        A, B, C = move(n - 1, m, A, bb, cc)

        if A[0] == "A" and C[0] == "B":
            B.append(A.pop())
        elif A[0] == "B" and C[0] == "C":
            C.append(B.pop())
        elif A[0] == "A" and C[0] == "C":
            C.append(A.pop())
        elif A[0] == "C" and C[0] == "B":
            B.append(C.pop())
        elif A[0] == "B" and C[0] == "A":
            A.append(B.pop())
        elif A[0] == "C" and C[0] == "A":
            A.append(C.pop())
        print("move %d from  %s to %s" % (n, A[0], C[0]))
        print("|  |  |")
        printPole(m, A, B, C)

        aa, bb = A.copy(), B.copy()
        aa[0], bb[0] = B[0], A[0]
        A, B, C = move(n - 1, m, aa, bb, C)

        A[0], C[0] = C[0], A[0]
        return A, B, C


n = int(input("Enter Input : "))
a = ["A"]
b = ["B"]
c = ["C"]
a += list(range(n, 0, -1))

print("|  |  |")
printPole(n, a, b, c)
move(n, n, a, b, c)
