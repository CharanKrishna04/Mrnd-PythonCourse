__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given a sequence [a1, ... ,an], the diff sequence is [|a1- a2|, |a2-a3|, .... |an -a1|] (loop around at the end).
(|x| denotes absolute value of x)

A sequence of 0s is called a null sequence.  

If we apply the diff process repeatedly on a given sequence, it may or may not end in a null sequence. 
For e.g. 
 - [1, 1, 1] becomes [0, 0, 0] in 1 step. 
 - [1, 1, 0] loops and never becomes a null sequence.

Write a routine to find out the number of steps it takes for a sequence to end in a null sequence. If it does not 
end (due to some repetition), then return -1.

Notes:
1. Assume nums is a valid list of integers.
2. Refer to the testcase for an example.
3. Write your own tests and edge cases, don't rely only on the examples given.
4. Feel free to write additional helper methods as appropriate.
5. Treat this as a coding problem, don't try to find O(1) maths formulas :) 
'''

# assume numbers is a valid list of numbers


def count_steps(numbers):
    if numbers == None:
        return -1
    if len(numbers)==0:
        return -1
    n=len(numbers)
    temp=list(numbers)
    end=[0]*n
    count=0
    while True:
        first=temp[0]
        for i in range(n):
            if i==n-1:
                temp[i]=abs(temp[i]-first)
            else:
                temp[i]=abs(temp[i]-temp[i+1])
        count+=1

        if end==temp:
            return count
        elif temp==numbers:
            return -1


# one basic test given, write more exhaustive tests
def test_count_steps():
    assert 1 == count_steps([1, 1, 1])
    assert -1==count_steps([1,1,0])
