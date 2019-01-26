import math


def factorize(number):
    if number<0:
        raise ValueError
    if not isinstance(number,int):
        raise TypeError
    result={}
    j=2
    while number>1:
        for i in range(j,int(math.sqrt(number+0.05))+1):
            if number%i==0:
                number=number/i
                j=i
                if i in result:
                    result[i]+=1
                else:
                    result[i]=1
                break
        else:
            if number>1:
                if number in result:
                    result[number]+=1
                else:
                    result[number]=1
                break

    return list(zip(result.keys(),result.values()))

def get_hcf(first, second):
    first=dict(first)
    second=dict(second)
    result={i:min(first[i],second[i]) for i in first if i in second}
    return list(zip(result.keys(), result.values()))

def get_lcm(first, second):
    first = dict(first)
    second = dict(second)
    result=dict()
    for i in first:
        if i in second:
            result[i]=max(first[i],second[i])
        else:
            result[i]=first[i]
    for i in second:
        if i not in first:
            result[i]=second[i]
    result=list(zip(result.keys(),result.values()))
    result.sort()
    return result

def multiply(first, second):
    first=dict(first)
    second=dict(second)
    result=dict()
    result={i: first[i]+second[j] for i in first for j in second if i==j }
    for i in first:
        if i not in result:
            result[i]=first[i]
    for i in second:
        if i not in result:
            result[i]=second[i]
    result = list(zip(result.keys(), result.values()))
    result.sort()
    return result
