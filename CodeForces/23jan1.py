for _ in range(int(input())):
    l1,r1,l2,r2=map(int,input().strip().split())
    if l1==r2:
        print(r1,l2)
    else:
        print(l1,r2)


