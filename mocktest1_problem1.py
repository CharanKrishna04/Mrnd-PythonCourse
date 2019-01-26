__author__ = 'Kalyan'

max_marks = 25

problem_notes ='''
Write a routine to sort the given list of numbers according to the number
of prime factors it has.

Constraints:
1. 1 and 0 are considered to have 0 factors
2. For negative numbers, the factor count of the corresponding
   positive numbers is considered for sorting
3. Numbers with more factors come before numbers with fewer factors
4. In case of a tie, bigger numbers (numerically) comes first
5. Return a new sorted list of numbers (not-inplace)
6. Refer to the testcase for an example.

Notes:
1. Use the python built in sorting functionality to get this done.
2. Write additional helper routines as required.
3. Assume that input is valid list of numbers.
'''
from math import sqrt
def factors_len(el):
    if el<0:
        el=abs(el)
    if el==0 or el==1:
        return 0
    result = set()
    j = 2
    while el > 1:
        for i in range(j, int(sqrt(el + 0.05)) + 1):
            if el % i == 0:
                el = el / i
                j = i
                result.add(i)
                break
        else:
            if el > 1:
                result.add(el)
                break
    return len(result)
# assume numbers is a valid list of numbers
def sort_by_factor_count(numbers):
    if numbers==None:
        return None
    temp=list(numbers)
    temp.sort(reverse=True)
    temp.sort(key=factors_len,reverse=True)
    return temp

# one basic test given, write more exhaustive tests
def test_sort_by_factor_count():
    # 10 has 2 factors [2,5] , 6 has 2 [2,3], 8 has 1 [2] and 2 has 1 [2], hence the result
    assert [10, 6, 8, 2] == sort_by_factor_count([2, 8, 6, 10])
    '''for testing
        1. IN-PLACE 
        2. ONE AND ZERO 
        3. NEGATIVE NUMBERS
        4. MULTIPLE DIGITS BOTH POSITIVE AND NEGATICE
        5. TIE BETWEEN NO. OF FACTORS
        
    '''
    input=[0,-1,2,-3,4,-5,6,-7,8,-9,1,1,-2]
    assert [6, 8, 4, 2, -2, -3, -5, -7, -9, 1, 1, 0, -1] == sort_by_factor_count(input)
    assert input==[0,-1,2,-3,4,-5,6,-7,8,-9,1,1,-2]

    #input is none
    assert None==sort_by_factor_count(None)

    #input is empty
    assert []==sort_by_factor_count([])

    #input is very big
    assert [84572855782975239485, 118837382974792839, 238832748245295]==sort_by_factor_count([118837382974792839,238832748245295,84572855782975239485])





