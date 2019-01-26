
for _ in range(int(input())):
    s = 'abcdefghijklmnopqrstuvwxyz'
    n,k=map(int,input().strip().split())
    s=s[:k]*(n//k+1)
    res=s[:n]
    print(res)

