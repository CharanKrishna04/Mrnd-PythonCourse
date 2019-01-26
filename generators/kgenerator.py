'''
For this problem you have to implement a generator which returns all k digit 
numbers whose sum of digits is n. 

Note that you must not generate the entire solution set at one go (ie) the 
result should be generated on demand (when next is called on generator). This means that 
I can call it with large values of n and k like 1000 and 500 and still 
its use of memory must be modest.

Notes:
1. raise TypeError if n and k are not ints.  
2. if n or k are not positive, raise ValueError 
3. the result numbers must be yield'ed in increasing order. 
4. you are free (encouraged :-) ) to define additional sub-routines as you see fit as long as you do not   
   violate the generator semantics given above

Examples:
 for n = 2 and k = 2, the generator must yield 11, 20 in that order
 for n = 4 and k = 2, the generator must yield 13, 22,31,40 in that order
 
Note that numbers starting with 0 are not valid For e.g. 02 is not a valid 2 digit number
'''

from itertools import product

#Implement this generator.
def kdigitnums(n, k):
    """
    This is a generator returns all k digit numbers whose sum is n. The numbers are yielded in
    increasing order
    """
    if k==1:
        yield n
    else:

        for i in [int(''.join(map(str,x))) for x in product(range(n),repeat=k) if x[0]!=0 and sum(x)==n]:
            yield i


        yield n * 10**(k-1)



# write more tests
def test_kdigitnums():

    print(list(kdigitnums(2,2)))
    assert [11, 20] == list(kdigitnums(2,2))
    print(list(kdigitnums(5, 3)))
    assert[104, 113, 122, 131, 140, 203, 212, 221, 230, 302, 311, 320, 401, 410, 500] == list(kdigitnums(5, 3))


    try:
        assert [] == list(kdigitnums(0, -2))
    except ValueError as e:
        pass

    try:
        assert [] == list(kdigitnums("shantanu","b"))
    except TypeError:
        pass

