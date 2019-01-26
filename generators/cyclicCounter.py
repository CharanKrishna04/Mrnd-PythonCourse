'''
This problem involves writing an iterator class that implements a CyclicCounter that take a value
and returns values descending down to 0 and then back to the value infinitely.

For e.g. for bound = 3. the iterator next() cycles through the values 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, ....

Notes:
- implement the methods of the class so that it behaves like an iterator with behavior described above
- a non positive value should raise ValueError
- no type checking required.
- you must use a constant amount of memory irrespective of the counter starting value (ie) I should be able to use
  really large values without running out of memory etc.
'''


class CyclicCounter(object):

    def __init__(self,object):
        if object <= 0 :
            raise ValueError
        self.flag=-1
        self.n=object+1
        self.temp=object

    def __iter__(self):
        return self

    def __next__(self):

        if self.n ==self.temp+1:
            self.flag = -1
        if self.n == 0:
            self.flag = 1
        self.n=self.n + self.flag
        return self.n


# a basic test is given, write your own tests.
def test_counter():
    c = CyclicCounter(2)
    # test the 1st 5 values, write
    i = 0
    result = []
    while i < 5:
        result.append(c.__next__())
        i += 1
    assert [2,1,0,1,2] == result
