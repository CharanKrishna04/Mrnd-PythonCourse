n=int(input())
l=list(map(int,input().strip().split()))
x=max(l)
l.remove(x)
while len(l)!=0:
    y=max(l)
    if x%y==0:
        if x==y:
            break
        else:
            if l.count(y)==2:
                break
            else:
                l.remove(y)
                continue
    else:
        break
print(x,y)