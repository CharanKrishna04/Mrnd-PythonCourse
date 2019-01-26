import sys
from random import randint
x=randint(1,3)
print(x)
sys.stdout.flush()
y=int(input())
if (x==1 and y==2) or (x==2 and y==1):
    print(3)
elif (x==1 and y==3) or (x==3 and y==1):
    print(2)
else:
    print(1)
sys.stdout.flush()