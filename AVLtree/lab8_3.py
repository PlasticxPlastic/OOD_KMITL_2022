def re(n):
    if m[n] != -1:
        return m[n]
    re(2*n+1)
    re(2*n+2)
    m[n] = min(m[2*n+1],m[2*n+2])
    m[2*n+1] -= m[n]
    m[2*n+2] -= m[n]
a,b = input('Enter Input : ').split('/')
a,b = int(a),list(map(int,b.split()))
if len(b) == a//2+1:
    m = [-1]*a
    for i in range(len(b)):
        m[a//2+i] = b[i]
    re(0)
    print(sum(m))
else:
    print('Incorrect Input')