def mycount(n,x,y,d):
    c1 = 0
    p1 = x
    f1 = -1

    while p1 <= n and p1 != y:
        p1 = p1 + d
        c1 += 1
    if p1 == y:
        f1=c1
    p1 = n
    while p1 >= 1 and p1 != y and f1==-1:
        p1 = p1 - d
        c1 += 1
    if p1 == y:
        f1 = c1
    p1 = 1
    while p1 <= n and p1 != y and f1==-1:
        p1 = p1 + d
        c1 += 1
    if p1 == y:
        f1=c1


    c1 = 0
    p1 = x
    f2=-1
    while p1 >= 1 and p1 != y:
        p1 = p1 - d
        c1 += 1
    if p1 == y:
        f2=c1
    p1 = 1
    while p1 <= n and p1 != y and f2==-1:
        p1 = p1 + d
        c1 += 1
    if p1 == y:
        f2 = c1
    p1 = n
    while p1 >= 1 and p1 != y and f2==-1:
        p1 = p1 - d
        c1 += 1
    if p1 == y:
        f2 = c1
    return min(f1,f2)

nu=int(input())
for i in range(nu):
    n,x,y,d=map(int,input().strip().split(' '))
    print(mycount(n,x,y,d))