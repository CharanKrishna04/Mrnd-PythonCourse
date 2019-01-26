'''
A number is said to be a magic number in a given base if it is divisible by sum of its digits in that given base.

A few examples:

11 -> is not a magic number in base 10 (since 11 is not divisible by 2)
11 -> is a magic number in base 16 (since 11 in hex is B and sum of digits is 11 (B) and since 11 is divisible by 11)
11 -> is not a magic number in base 2 -> (11 in binary is 1011, sum of digits is 3 and 11 is not divisible by 3)
33 -> is a magic number in base 12 ( it is 29 in base 12, sum of digits is 11 and 33 is divisible by 11)
33 -> is not a magic number in base 10 ( since 33 is not divisible by 6)
255 -> is not a magic number in base 16 (255 is FF in hex, sum of digits is 30, 255 is not divisible by 30)
66 -> is a magic number in base (66 is 12 in base 64, sum of digits is 3, and 66 is divisible by 3)

Write the following routines to determine if a given number is a magic number in a given base and to write
an infinite generator of successive magic numbers in a given base.

Constraints:
- no type checking required.
- raise value error if number <=0 or base < 2
- there is no upper bound on the base, so code appropriately instead of assuming that is less than some hardcoded
upper bound value like 16 or 36.
'''

import string


def convert(number, base):


    c=string.digits+string.ascii_lowercase
    #res=''
    res=[]
    while number:
        #res=c[number%base]+res
        res.insert(0,number%base)
        number=number//base

    return res

# returns True if the specified number is a magic number in the given base.
def is_magic(number, base):
    
    return number%sum(convert(number,base))==0

# generator that yields the magic numbers in a given base starting from 1 in increasing order.
# use the above method to get this done.
def magic_numbers(base):

    i=1
    while True:
        if is_magic(i,base):
            yield i
        i+=1



# write your own tests.
def test_is_magic():
    assert True == is_magic(11,16)
    assert False == is_magic(11, 10)
    assert True == is_magic(33, 12)
    assert True == is_magic(66, 64)
    assert False == is_magic(255, 16)


def test_magic_numbers():
    l=[]
    m=magic_numbers(12)
    for i in range(100):
        l.append(next(m))
    print(l)

