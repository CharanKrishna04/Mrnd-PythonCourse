def diff(s1,s2):
    c=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            c+=1
    return c
n=int(input())
s=input().strip()
t1='RGB'*((n//3)+1)
t1=t1[0:n]
t2='GBR'*((n//3)+1)
t2=t2[0:n]
t3='BrG'*((n//3)+1)
t3=t3[0:n]
t4='BGR'*((n//3)+1)
t4=t4[0:n]
t5='RBG'*((n//3)+1)
t5=t5[0:n]
t6='GRB'*((n//3)+1)
t6=t6[0:n]
ans=diff(t1,s)
res=t1
t=diff(t2,s)
if t<ans:
    ans=t
    res=t2
t=diff(t3,s)
if t<ans:
    ans=t
    res=t3
t=diff(t4,s)
if t<ans:
    ans=t
    res=t4
t=diff(t5,s)
if t<ans:
    ans=t
    res=t5
t=diff(t6,s)
if t<ans:
    ans=t
    res=t6
print(ans)
print(res)
