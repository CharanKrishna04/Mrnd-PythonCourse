'''
 For this problem, you will write simple infinite generators for primes and fibonacci numbers.

 In addition you will write a simple generator common_elements function which returns the
 intersection of 2 given sorted iterators/iterables

'''

# Returns a generator which returns the sequence of primes infinitely.
# returns 2, 3, 5, 7, 11, 13,  ... successively


def primes():
    yield 2
    yield 3
    num=4
    while True:
        num+=1
        if num%2==0 or num%3==0:
            continue
        i=5
        w=2
        f=0
        while i*i<=num:
            if num%i == 0:
                f=-1
                break
            i=i+w
            w=6-w
        if f==0:
            yield num
# Returns a generator which returns the sequence of fibonacci numbers infinitely
def fibonacci_numbers():

    l1=0
    yield 1
    l2=1

    while True:
        n=l1+l2
        yield n
        l1=l2
        l2=n
# 1, 1, 2, 3, 5, 8, 13, ... successively (note that you should start from 1, 1 and not 0, 1)

# This is a generator which returns the common elements in both the first and second sorted iterators/iterables. If first
# and second are infinite, then this is also infinite. Assume that both first and second are sorted in ascending order.
# A simple use case for this is to find fibonacci numbers which are also primes using the two generators given above.
# It should work for any sorted iterator or iterable, so code accordingly.
#
# No special error checking required, allow errors to percolate up on wrong inputs.
def common_elements(seq1, seq2):

    x=next(seq1)
    y=next(seq2)
    while True:

        if x==y:
            yield x
            x=next(seq1)
            y=next(seq2)
        elif x<y:
            x=next(seq1)
        elif x>y:
            y=next(seq2)






# write your own tests.
def test_primes():
    pass


def test_fibonacci():
    pass

def test_common_elements():

    pass

