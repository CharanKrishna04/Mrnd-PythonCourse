from math import inf
n,q=map(int,input().strip().split())
a=list(map(int,input().strip().split()))
seg=[]
for i in range(q):
    s,e=map(int,input().strip().split())
    seg.append([s,e])
i=0
q1=q
ans=0
ansco=0
anscom=[]
while (i<(1<<q1)):
    com=[]
    res = list(a)
    res.append(0)
    res.append(0)
    ones=0
    for j in range(q1):
        if (i>>j)&1:
            ones+=1
            res[seg[j][0]]=-1
            res[seg[j][1]+1]=1
            com.append(j+1)
    mi=inf
    ma=-inf
    curSum=0
    for j in res:
        curSum+=j
        mi=min(mi,curSum)
        ma=max(ma,curSum)
    if ans<ma-mi:
        ans-ma-mi
        ansco=ones
        anscom=com

    i+=1
print(ans)
print(ansco)
print(*anscom)


