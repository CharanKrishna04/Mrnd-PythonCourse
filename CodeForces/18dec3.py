def findIndex(l,s):
    try:
        i=l.index(s)
        return i
    except ValueError as ae:
        return -1

n=int(input())
l=[]
m=[]
ans=[]
res=['.']*(2*n-2)
for i in range(2*n-2):
    s=input()
    if len(s)==n-1:
        m.append(s)
    l.append(s)
if (m[0]+m[1][-1])==(m[0][0]+m[1]):
    ans.append(m[0][0]+m[1])
if (m[1][0]+m[0])==(m[1]+m[0][-1]):
    ans.append(m[1]+m[0][-1])
'''if len(ans)==1:
    ans=ans[0]
    for i in range(len(ans)):
        j=findIndex(l,ans[:i])
        res[j]='P'
        '''

try:
    temp=list(l)
    for i in range(1,len(ans[0])):
        j=temp.index(ans[0][:i])
        temp[j]='.'
        res[j]='P'
    for i in range(1,len(ans[0])):
        j=temp.index(ans[0][i:])
        temp[j]='.'
        res[j]='S'

except ValueError:
    res = ['.'] * (2 * n - 2)
    temp = list(l)
    for i in range(len(1,ans[1]) ):
        j = temp.index(ans[1][:i])
        temp[j] = '.'
        res[j] = 'P'
    for i in range(1, len(ans[1])):
        j = temp.index(ans[1][i:])
        temp[j] = '.'
        res[j] = 'S'
print(''.join(res))

