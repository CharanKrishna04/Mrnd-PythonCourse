'''
Return the top n most frequently occurring chars and their respective counts
e.g aaaaaabbbbcccc, 2 should return [(a 5) (b 4)]
in case of a tie, return char which comes earlier in alphabet ordering
e.g. cdbba,2 -> [(b,2) (a,1)]
use standard types and and builtin functions we have used in the course.

constraints:
1. raise TypeError if word is not a str or n is not an int
2. raise ValueError if n <= 0,
3. if n > number of unique chars just return the available chars and their counts
2. The function should be case sensitive (ie) A and a are different. So aaAABBB, 2 should return [(B,3), (A,2)]
'''

def top_chars(word, n):
    if not isinstance(word,str) or not isinstance(n,int):
        raise TypeError
    if n<=0:
        raise ValueError
    d=dict()
    l=set(word)
    for i in l:
        d[i]=word.count(i)
    d=list(d.items())
    d.sort(key=lambda a:a[0])
    d.sort(key=lambda a:a[1],reverse=True)
    return d[:n]



#write your own tests.
def test_top_chars():

    assert [('a',5),('b',4)] == top_chars("aaaaabbbbcccdde", 2)