import sys
n,r=map(int,input().strip().split())
for i in range(n):
    x=int(input())
    if x<r:
        print("Bad boi")
    else:
        print("Good boi")
    sys.stdout.flush()
