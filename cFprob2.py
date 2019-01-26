n=int(input())
s=list(input())
mcount=0
scount=0
i=0
while i<n:

    if s[i]=='G':
        scount+=1
    else:
        if i<n-1 and s[i]=='G':
            scount+=2
            i+=1
        else:
            mcount = max(scount, mcount)
            scount=0