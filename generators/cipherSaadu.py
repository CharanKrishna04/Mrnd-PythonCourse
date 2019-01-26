'''
 This is another custom encryption scheme that was in popular use to send secret messages in olden days. In this
 scheme successive letters are written in different lines by hand and all the characters are merged line by line
 to create the final encrypted text. The number of lines can differ and is an input to this problem.

 Write encode and decode routines for this cipher given a text and the number of lines n.

 E.g "Hello Cat" with line count 2 when written over 2 lines is:
line1:              H   l   o    C   t
line2:                e   l   ' '  a

            
    So final text is "HloCtel a" (characters of line 1 followed by characters of line2)

Similarly a word "Popular" with line count 3 will be
line1:            P       l
line2:              o   u   a
line3:                p       r

    So final text is Plouapr

Constraints and notes:
1. Write the cipher routines work for arbitrary n. Raise value error if n <= 0
2. Assume types are correct
3. Note that the encryption is not done word by word but for the whole text at one go. See the "Hello cat" example, the
   space was treated as part of text and it moved.
4. Make good use of python builtins and data structures. Note that successive characters will go into lines
   1, 2, 3, 2, 1, 2, 3, 2, 1, ... for n=3 (repeating pattern)
5. Note that you are writing a program to solve this, so you can just use plain code and additional data structures
   to solve this instead of finding mathematical patterns (that is also allowed :-) ).
    
'''

def nexte(n):
    count=0
    while True:
        while count<n:
            count+=1
            yield count
        while count>1:
            count-=1
            yield count

def arrange_in_line(text,n):
    y = nexte(n)
    lines = [''] * n
    for i in text:
        j = next(y)
        lines[j - 1] += str(i)
    return lines

def encode(text,n):
    if n<=0:
        raise ValueError
    lines = arrange_in_line(text,n)
    return ''.join(lines)
    
def lines_split(text,lines):
    l=[]
    for i in lines:
        l.append(text[:len(i)])
        text=text[len(i):]

    return l

def decode(text, n):
    if n<=0:
        raise ValueError
    lines = arrange_in_line(text,n)
    lines = lines_split(text,lines)
    y=nexte(n)
    res=''

    for i in range(len(text)):
        j=next(y)
        res=res+lines[j-1][0]
        lines[j-1]=lines[j-1][1:]

    return res


# write your own tests.
def test_encode():
    assert 'Plouapr' == encode("Popular",3)
    assert "hloctel a" == encode("hello cat", 2)
    assert 'hotel alc' == encode("hello cat", 3)


def test_decode():
    assert 'Popular' == decode("Plouapr", 3)
    assert 'hello cat' == decode("hloctel a", 2)
    assert 'hello cat' == decode("hotel alc", 3)

