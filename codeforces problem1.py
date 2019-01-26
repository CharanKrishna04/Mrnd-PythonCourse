
def mygen1(x,d,n):
    dir=1
    while True:
        while dir==1:
            x=x+d
            if x>n:
                x=n
                dir=-1
            yield x
        while dir == -1:
            x=x-d
            if x<1:
                x=1
                dir=1
            yield x
def mygen2(x,d,n):
    dir=-1
    while True:
        while dir == -1:
            x=x-d
            if x<1:
                x=1
                dir=1
            yield x
        while dir==1:
            x=x+d
            if x>n:
                x=n
                dir=-1
            yield x
nu=int(input())
for i in range(nu):
    n,x,y,d=map(int,input().strip().split(' '))
    count=0
    flag=0
    c1=x
    c2=x
    d1=mygen1(x,d,n)
    d2=mygen2(x,d,n)
    while flag==0:
        count+=1
        c1=next(d1)
        c2=next(d2)
        if c1==y or c2==y:
            print(count)
            flag=3
            break
        if c1==x:
            flag=1
        if c2==x:
            flag=2
    while flag==1:
        count+=1
        c2=next(d2)
        if c2==y:
            print(count)
            flag=3
        if c2==x:
            flag=2
    while flag==2:
        count+=1
        c1=next(d1)
        if c1==y:
            print(count)
            flag=3
        if c1==x:
            flag=1
    if flag !=3:
        print(-1)


