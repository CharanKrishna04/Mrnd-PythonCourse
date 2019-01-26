n=int(input())
s=input().strip()
l=[]
for i in range(n-1):
    if s[i]==s[i+1]:
        l.append(-1)
    else:
        l.append(0)
#for i in range(n-1):
