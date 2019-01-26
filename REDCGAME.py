


def problem():
    t=int(input())
    for i in range(t):
        n,k=map(int,input().split())
        a=list(map(int,input().split(' ')))
        if len(a)==1:
            print(a[0])
        else:
            a.sort()
            for j in range(n-1):

                if a[j]>k:
                    x=a[j] - k
                    a[j] -= x
                    a[j + 1] -= x
            print(sum(a))

problem()
