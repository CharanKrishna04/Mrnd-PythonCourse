n=int(input())
l=list(map(int,input().strip().split()))
m=max(l)
i=0
flag=0
while len(set(l))!=1:
    i=i%n
    if (i==0 and l[i]<l[i+1]) or (i==n-1 and l[i-1]>l[i]) or (l[i-1]>l[i] and l[i]<l[i+1]) :
        print('NO')
        flag=-1
        break
    if l[i]!=m and l[i]==l[i+1]:
        l[i]+=1
        l[i+1]+=1
        i+=1
    i+=1
if flag==0:
    print('YES')