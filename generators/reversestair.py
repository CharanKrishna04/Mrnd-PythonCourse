'''
This problem is the reverse of stair. Given the jumbled text created 
according to the rules given in stair and number of steps, create the original text.

Notes:
1. Raise ValueError if n <= 0
2. Raise TypeError if text is not a str
3. Do not search for mathematical patterns, solve this programatically
'''

def sequence(n):

    while True:
        i=n
        while i>0:
            yield i
            i-=1
        i+=1
        while i<=n:
            yield i
            i += 1
def jumble(text, n):
    steps=['']*n
    n=sequence(n)
    c=0
    while text:
        x=next(n)
        steps[x-1]+=text[:x]
        c+=1
        text=text[x:]

    return steps,c

def split_steps(text,steps):
    res=[]
    for i in steps:
        l=len(i)
        res.append(text[:l])
        text=text[l:]
    return res
def unjumble(jumbled_text, n):

    steps,c=jumble(jumbled_text,n)
    steps=split_steps(jumbled_text,steps)
    y=sequence(n)
    result=''
    for i in range(c):
        x=next(y)
        result += steps[x-1][:x]
        steps[x-1]=steps[x-1][x:]
    return result



def test_unjumble():
    print(unjumble('hoAskan',2))
    assert "Ashokan" == unjumble("hoAskan", 2)