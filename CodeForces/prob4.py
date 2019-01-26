import sys
n,c=map(int,input().strip().split())
m=1000
low=1
high=n
while((low<high) and (m>0)):
    mid=low+(high-low)//2
    print(1,mid)
    sys.stdout.flush()
    m-=1
    res=int(input())
    if res==1:
        high=mid
        if high==low or (m-c)<0:
            continue
        print(2)
        sys.stdout.flush()
        m-=c
    elif res==0:
        low=mid+1
print(3,high)
sys.stdout.flush()