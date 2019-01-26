def mygenl(p, l, v):
    low=p-v
    high=p+v
    if low<0:
        low=0
    if high>=l:
        high=l-1
    while True:
        while(p>low):
            p-=1
            yield p
        while (p < high):
            p += 1
            yield p
def testcase(s):

    l = len(s)
    objs = []
    res = []
    for i in range(l):
        if s[i] != '.':
            objs.append(mygenl(i, l, int(s[i])))
            res.append(i)
    if len(res)==0 or len(res)==1:
        return True
    for i in range(l * 5):
        for j in range(len(res)):
            res[j] = objs[j].__next__()
            if res.count(res[j]) > 1:
                return False
    return True
def problem():
    n = int(input())
    for i in range(n):
        s = input()
        if(testcase(s)):
            print('safe')
        else:
            print('unsafe')
problem()



