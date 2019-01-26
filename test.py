from math import sqrt
from math import log10


def zero(x):
    while (x):
        if x % 10 == 0:
            return True
        x = x // 10
    return False


def valid(x):
    if zero(x):
        return False
    for i in range(int(log10(x)), 0, -1):
        if prime[x % (10 ** i)] == False:
            return False#no fear
    return True#fears


prime = [True] * 1000002
prime[0] = False
prime[1] = False
for i in range(2, int(sqrt(1000002)) + 1):
    for j in range(i * i, 1000002, i):
        prime[j] = False
fear = []
cf = 0
for i in range(int(sqrt(1000002)) + 1):
    if prime[i]:
        if valid(i):
            cf += 1
    fear.append(cf)

for _ in range(int(input())):
    n = int(input())
    print(fear[n])