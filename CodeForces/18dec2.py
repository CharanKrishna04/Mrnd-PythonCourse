n=int(input())
l=list(map(int,input().strip().split()))
l.sort()
res=0
for i in range(0,n,2):
    res+=l[i+1]-l[i]
print(res)